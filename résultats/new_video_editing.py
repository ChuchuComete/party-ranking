import asyncio
import re
import aiohttp
import subprocess
import sys
import os
import time
from typing import List, Literal, Tuple, TypedDict
from yt_dlp import YoutubeDL

VERSION = "2.0.0"
print(f"new_video_editing.py version {VERSION}")

CDN = ['catbox', 'animemusicquiz.com', 'prlive-static.frederic94500.net']

width = 1280
height = 720
transition_duration = 0.5


class FileInfo(TypedDict):
    videoFile: str
    audioFile: str
    duration: float


def get_gpu_type() -> Literal["nvidia", "amd", "intel", None]:
    try:
        # Check for Nvidia GPU
        nvidia_output = subprocess.check_output(
            "nvidia-smi", shell=True, stderr=subprocess.STDOUT)
        if "NVIDIA" in nvidia_output.decode():
            return "nvidia"
    except subprocess.CalledProcessError:
        pass

    try:
        # Check for AMD GPU
        amd_output = subprocess.check_output(
            "lspci | grep -i 'vga.*amd'", shell=True, stderr=subprocess.STDOUT)
        if "AMD" in amd_output.decode():
            return "amd"
    except subprocess.CalledProcessError:
        pass

    try:
        # Check for Intel GPU
        intel_output = subprocess.check_output(
            "lspci | grep -i 'vga.*intel'", shell=True, stderr=subprocess.STDOUT)
        if "Intel" in intel_output.decode():
            return "intel"
    except subprocess.CalledProcessError:
        pass

    return None


def youtube_dl(link: str, output_name: str):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': f'{output_name}',
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }]
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


async def download_file(session, url, filename):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                with open(filename, 'wb') as file:
                    file.write(await response.read())
            else:
                print(f"Failed to download {url}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")


async def download_async(songs):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, song in enumerate(songs):
            link = song.link
            print("Downloading: " + link)
            if any([domain in link for domain in CDN]) and not os.path.exists(f'temp/{i+1}.{song.extension}'):
                tasks.append(download_file(
                    session, link, f'temp/{i+1}.{song.extension}'))
            elif 'youtu' in link and not os.path.exists(f'temp/{i+1}.mp4'):
                tasks.append(asyncio.to_thread(
                    youtube_dl, link, f'temp/{i+1}.mp4'))
        await asyncio.gather(*tasks)


def download(songs):
    asyncio.run(download_async(songs))

#def get_file_length(file, local_binary_folder) -> float:
#    result = subprocess.check_output(
#        f'{local_binary_folder}ffprobe -i {file} -show_entries format=duration -v quiet -of csv="p=0"',
#        shell=True
#    )
#    return float(result.strip())

def get_file_length(file, local_binary_folder, stream_type='v') -> float:
    """Gets duration from stream level rather than container level to avoid rounding mismatches."""
    selector = f'{stream_type}:0'
    result = subprocess.check_output(
        f'{local_binary_folder}ffprobe -i {file} -select_streams {selector} '
        f'-show_entries stream=duration -v quiet -of csv="p=0"',
        shell=True
    )
    val = result.decode().strip().splitlines()[0]
    return float(val)

def verify_sample(songs, local_binary_folder) -> bool:
    """Vérifie si la durée de l'échantillon est correcte et ne dépasse pas la durée de la vidéo."""
    status = True
    for i, song in enumerate(songs):
        print(i + 1, "-", song.info)
        file = f'temp/{i + 1}.webm' if os.path.exists(
            f'temp/{i + 1}.webm') else f'temp/{i + 1}.mp4'
        result = subprocess.check_output(
            f'{local_binary_folder}ffprobe -i {file} -show_entries format=duration -v quiet -of csv="p=0"',
            shell=True
        )
        file_duration = float(result.strip())
        if song.sample + song.sample_length > file_duration:
            status = False
            print(
                f"❌ Sample duration exceeds video duration for {song.info}, sample: {song.sample + song.sample_length} > video: {file_duration}")
        else:
            print(f"✅ Sample duration is correct for {song.info}")
    return status


def verify_preprocess_files(songs, local_binary_folder) -> Tuple[List[FileInfo], bool]:
    """Vérifie si les fichiers prétraités existent déjà."""
    status = True
    files: List[FileInfo] = []
    for i in range(len(songs), 0, -1):
        song = songs[i-1]
        print(i, "-", song.info)

        output_video = f'temp/{i}_processed.mp4'
        output_audio = f'temp/{i}_audio.wav'

        if not os.path.exists(output_video):
            status = False
            print(f"Missing video file: {output_video}")
        if not os.path.exists(output_audio):
            status = False
            print(f"Missing audio file: {output_audio}")

        result_video = subprocess.check_output(
            f'{local_binary_folder}ffprobe -i {output_video} -show_entries format=duration -v quiet -of csv="p=0"',
            shell=True
        )
        song_duration = float(result_video.strip())
        result_audio = subprocess.check_output(
            f'{local_binary_folder}ffprobe -i {output_audio} -show_entries format=duration -v quiet -of csv="p=0"',
            shell=True
        )
        if abs(float(result_audio.strip()) - song_duration) > 0.1:
            status = False
            print(f"Audio and video duration mismatch for {output_video}")
        files.append({"videoFile": output_video,
                     "audioFile": output_audio, "duration": song_duration})

    return files, status


def verify_part_files(local_binary_folder) -> List[FileInfo]:
    """Vérifie si les fichiers de parties existent déjà."""
    files: List[FileInfo] = []
    i = 1
    while True:
        output_file = f"part{i}.mp4"
        if not os.path.exists(output_file):
            break
        result = subprocess.check_output(
            f'{local_binary_folder}ffprobe -i {output_file} -show_entries format=duration -v quiet -of csv="p=0"',
            shell=True
        )
        video_duration = float(result.strip())
        files.append({"videoFile": output_file, "duration": video_duration})
        i += 1
        
    if len(files) == 0:
        print("No part files found")
        raise Exception("No part files found")

    return files

#def preprocess_videos(songs, encoder: str, quality: str, threads: int, local_binary_folder, verbose="") -> List[FileInfo]:
#    """Prétraite chaque vidéo et applique les filtres nécessaires."""
"""
    files = []
    for i in range(len(songs), 0, -1):
        song = songs[i-1]
        print(i, song.info)

        input_video = f'temp/{i}.webm' if os.path.exists(
           f'temp/{i}.webm') else f'temp/{i}.mp4'
        overlay_image = f'temp/a{i}.png'
        output_video = f'temp/{i}_processed.mp4'
        output_audio = f'temp/{i}_audio.wav'

        if not os.path.exists(output_video):
            ffprobe_command = (
                f'{local_binary_folder}ffprobe -v error -select_streams v:0 -show_entries stream=width,height '
                f'-of csv=p=0:s=x {input_video}'
            )
            video_dimensions = subprocess.check_output(
                ffprobe_command, shell=True).decode().strip()
            input_width, input_height = map(int, video_dimensions.split('x'))

            input_aspect = input_width / input_height
            target_aspect = width / height
            
            if input_aspect > target_aspect:
                scale_width = width
                scale_height = int(width / input_aspect)
                pad_top = (height - scale_height) // 2
                pad_bottom = height - scale_height - pad_top
                pad_left, pad_right = 0, 0
            elif input_aspect < target_aspect:
                scale_width = int(height * input_aspect)
                scale_height = height
                pad_left = (width - scale_width) // 2
                pad_right = width - scale_width - pad_left
                pad_top, pad_bottom = 0, 0
            else:
                scale_width, scale_height = width, height
                pad_top, pad_bottom, pad_left, pad_right = 0, 0, 0, 0

            pad_filter = (
                f"scale={scale_width}:{scale_height},"
                f"pad={width}:{height}:{pad_left}:{pad_top}:black"
            )

            ffmpeg_command_video = (
                f'{local_binary_folder}ffmpeg {verbose} -ss {song.sample} -t {song.sample_length} -i {input_video} -i {overlay_image} '
                f'-filter_complex "[0:v]{pad_filter}[scaled];[1:v]scale={width}:{height}[overlay];'
                f'[scaled][overlay]overlay=x=0:y=0,fps=fps=23.976[output]" '
                f'-map "[output]" -c:v {encoder} {quality} -video_track_timescale 24000 '
                f'-an -threads {threads} {output_video}'
            )
            os.system(ffmpeg_command_video)
            
        if not os.path.exists(output_audio):
            ffmpeg_command_audio = (
                f'{local_binary_folder}ffmpeg {verbose} -ss {song.sample} -t {song.sample_length} -i {input_video} -vn -c:a pcm_s16le -af loudnorm -threads {threads} {output_audio}'
            )
            os.system(ffmpeg_command_audio)

        result_video = get_file_length(output_video, local_binary_folder)
        result_audio = get_file_length(output_audio, local_binary_folder)
        if abs(result_audio - result_video) > 0.1:
            print(f"Audio and video duration mismatch for {output_video}")
            sys.exit(1)
        files.append({"videoFile": output_video,
                     "audioFile": output_audio, "duration": result_audio})

    return files
"""

def preprocess_videos(songs, encoder: str, quality: str, threads: int, local_binary_folder, verbose="") -> List[FileInfo]:
    """Prétraite chaque vidéo et applique les filtres nécessaires."""
    files = []
    for i in range(len(songs), 0, -1):
        song = songs[i-1]
        print(i, song.info)

        input_video = f'temp/{i}.webm' if os.path.exists(
            f'temp/{i}.webm') else f'temp/{i}.mp4'
        overlay_image = f'temp/a{i}.png'
        output_video = f'temp/{i}_processed.mp4'
        output_audio = f'temp/{i}_audio.wav'

        if not os.path.exists(output_video):
            ffprobe_command = (
                f'{local_binary_folder}ffprobe -v error -select_streams v:0 -show_entries stream=width,height '
                f'-of csv=p=0:s=x {input_video}'
            )
            video_dimensions = subprocess.check_output(
                ffprobe_command, shell=True).decode().strip()
            input_width, input_height = map(int, video_dimensions.split('x'))

            input_aspect = input_width / input_height
            target_aspect = width / height
            
            if input_aspect > target_aspect:
                scale_width = width
                scale_height = int(width / input_aspect)
                pad_top = (height - scale_height) // 2
                pad_bottom = height - scale_height - pad_top
                pad_left, pad_right = 0, 0
            elif input_aspect < target_aspect:
                scale_width = int(height * input_aspect)
                scale_height = height
                pad_left = (width - scale_width) // 2
                pad_right = width - scale_width - pad_left
                pad_top, pad_bottom = 0, 0
            else:
                scale_width, scale_height = width, height
                pad_top, pad_bottom, pad_left, pad_right = 0, 0, 0, 0

            pad_filter = (
                f"scale={scale_width}:{scale_height},"
                f"pad={width}:{height}:{pad_left}:{pad_top}:black"
            )

            ffmpeg_command_video = (
                f'{local_binary_folder}ffmpeg {verbose} -ss {song.sample} -t {song.sample_length} -i {input_video} -i {overlay_image} '
                f'-filter_complex "[0:v]{pad_filter}[scaled];[1:v]scale={width}:{height}[overlay];'
                f'[scaled][overlay]overlay=x=0:y=0,fps=fps=23.976[output]" '
                f'-map "[output]" -c:v {encoder} {quality} -video_track_timescale 24000 '
                f'-an -threads {threads} {output_video}'
            )
            os.system(ffmpeg_command_video)
            
        if not os.path.exists(output_audio):
            ffmpeg_command_audio = (
                f'{local_binary_folder}ffmpeg {verbose} -ss {song.sample} -t {song.sample_length} -i {input_video} -vn -c:a pcm_s16le -af loudnorm -threads {threads} {output_audio}'
            )
            os.system(ffmpeg_command_audio)

        result_video = get_file_length(output_video, local_binary_folder, stream_type='v')
        result_audio = get_file_length(output_audio, local_binary_folder, stream_type='a')
        if abs(result_audio - result_video) > 0.5:
            print(
                f"Duration mismatch for {output_video}: "
                f"video={result_video:.3f}s  audio={result_audio:.3f}s  "
                f"expected≈{float(song.sample_length):.3f}s"
            )
            sys.exit(1)
        files.append({"videoFile": output_video,
                     "audioFile": output_audio, "duration": result_audio})

    return files

def concatenate_videos(files, part, threads, encoder, quality, local_binary_folder, verbose) -> List[FileInfo]:
    """Concatène les vidéos prétraitées avec des transitions."""
    filters = ""
    inputs = ""
    accumulated_offset = 0.0

    for idx, file in enumerate(files):
        inputs += f" -i {file['videoFile']}"
        if idx == 0:
            filters += f"[0:v]null[v0]; "
        else:
            accumulated_offset += files[idx -
                                        1]['duration'] - transition_duration
            filters += (
                f"[v{idx-1}][{idx}:v]xfade=transition=fade:duration={transition_duration}:offset={accumulated_offset}[v{idx}]; "
            )

    filters = filters.rstrip("; ")
    output_file = f"part{part}.mp4"

    command = (
        f"{local_binary_folder}ffmpeg {verbose} {inputs} -filter_complex \"{filters}\" "
        f"-map_metadata -1 -avoid_negative_ts make_zero -map \"[v{len(files)-1}]\" -c:v {encoder} {quality} -video_track_timescale 24000 -an -threads {threads} {output_file}"
    )

    print(command)
    os.system(command)

    result = subprocess.check_output(
        f'{local_binary_folder}ffprobe -i {output_file} -show_entries format=duration -v quiet -of csv="p=0"',
        shell=True
    )
    video_duration = float(result.strip())

    return {"videoFile": output_file, "duration": video_duration}


#def concatenate_audio(files, threads, local_binary_folder, verbose="") -> str:
#    """Concatène les fichiers audio."""
"""
    inputs = ""
    filters = ""
    accumulated_offset = 0.0

    for idx, file in enumerate(files):
        inputs += f" -i {file['audioFile']}"
        if idx == 0:
            filters = f"[0:a]afade=t=in:st=0:d={transition_duration}[a0]; "
        elif idx == len(files) - 1:
            accumulated_offset += files[idx -
                                        1]['duration'] - transition_duration
            filters += f"[a{idx-1}][{idx}:a]acrossfade=d={transition_duration}[a{idx}]; "
            accumulated_offset += files[idx]['duration'] - transition_duration
            filters += f"[a{idx}]afade=t=out:st={accumulated_offset}:d={transition_duration}[a{idx+1}]; "
        else:
            accumulated_offset += files[idx -
                                        1]['duration'] - transition_duration
            filters += f"[a{idx-1}][{idx}:a]acrossfade=d={transition_duration}[a{idx}]; "

    filters = filters.rstrip("; ")
    output_file = "output_audio.wav"

    command = (
        f"{local_binary_folder}ffmpeg {verbose} {inputs} -filter_complex \"{filters}\" "
        f"-map_metadata -1 -avoid_negative_ts make_zero -map \"[a{len(files)}]\" -c:a pcm_s16le -threads {threads} {output_file}"
    )

    print(command)
    os.system(command)

    print(f"Output file created: {output_file}")

    return output_file
"""
def concatenate_audio(files, threads, local_binary_folder, verbose="") -> str:
    """Concatène les fichiers audio en utilisant des batchs pour éviter les erreurs mémoire."""
    
    BATCH_SIZE = 10
    output_file = "output_audio.wav"

    def merge_batch(batch_files: list, output_path: str, fade_in: bool, fade_out: bool):
        """Merge a batch of files with crossfades, optional fade in/out."""
        inputs = ""
        filters = ""

        for idx, file in enumerate(batch_files):
            audio_path = file if isinstance(file, str) else file['audioFile']
            duration   = None if isinstance(file, str) else file['duration']
            inputs += f" -i {audio_path}"

            if idx == 0:
                if fade_in:
                    filters = f"[0:a]afade=t=in:st=0:d={transition_duration}[a0]; "
                else:
                    filters = f"[0:a]acopy[a0]; "
            else:
                filters += f"[a{idx-1}][{idx}:a]acrossfade=d={transition_duration}[a{idx}]; "

        last_label = f"a{len(batch_files) - 1}"

        if fade_out:
            accumulated = sum(
                (f['duration'] if not isinstance(f, str) else get_file_length(f, local_binary_folder, 'a'))
                for f in batch_files
            ) - transition_duration * (len(batch_files) - 1) - transition_duration
            out_label = f"a{len(batch_files)}"
            filters += f"[{last_label}]afade=t=out:st={accumulated}:d={transition_duration}[{out_label}]"
            last_label = out_label
        else:
            filters = filters.rstrip("; ")

        command = (
            f"{local_binary_folder}ffmpeg {verbose} {inputs} "
            f"-filter_complex \"{filters}\" "
            f"-map_metadata -1 -avoid_negative_ts make_zero "
            f"-map \"[{last_label}]\" -c:a pcm_s16le -threads {threads} {output_path}"
        )
        print(command)
        os.system(command)

    # --- Split into batches and merge progressively ---
    batches = [files[i:i+BATCH_SIZE] for i in range(0, len(files), BATCH_SIZE)]

    if len(batches) == 1:
        # Small enough to do in one pass
        merge_batch(batches[0], output_file, fade_in=True, fade_out=True)
    else:
        # First pass: merge each batch into a temp intermediate
        intermediates = []
        for batch_idx, batch in enumerate(batches):
            is_first = batch_idx == 0
            is_last  = batch_idx == len(batches) - 1
            temp_path = f"temp/intermediate_{batch_idx}.wav"

            merge_batch(
                batch,
                temp_path,
                fade_in=is_first,
                fade_out=is_last
            )
            # Wrap intermediate as a dict so it's compatible with merge_batch
            intermediates.append({
                'audioFile': temp_path,
                'duration': get_file_length(temp_path, local_binary_folder, 'a')
            })

        # Second pass: merge all intermediates into the final file
        # No fade in/out — already applied in the first pass
        merge_batch(intermediates, output_file, fade_in=False, fade_out=False)

    print(f"Output file created: {output_file}")
    return output_file

def final_concatenate(pr_name, final_videos, audio_file, local_binary_folder, threads, encoder, quality, audio_encoder="aac", webm=False, verbose=""):
    """Concatène les vidéos prétraitées avec des transitions."""
    filters = ""
    inputs = ""
    accumulated_offset = 0.0

    if len(final_videos) == 1:
        inputs += f" -i {final_videos[0]['videoFile']}"
        filters = f"[0:v]fade=t=in:st=0:d={transition_duration}[v0]; [v0]fade=t=out:st={final_videos[0]['duration'] - transition_duration}:d={transition_duration}[v1]; "
    else:
        for idx, file in enumerate(final_videos):
            inputs += f" -i {file['videoFile']}"
            if idx == 0:
                filters += f"[0:v]fade=t=in:st=0:d={transition_duration}[v0]; "
            elif idx == len(final_videos) - 1:
                accumulated_offset += final_videos[idx -
                                                   1]['duration'] - transition_duration
                filters += (
                    f"[v{idx-1}][{idx}:v]xfade=transition=fade:duration={transition_duration}:offset={accumulated_offset}[v{idx}]; "
                )
                accumulated_offset += final_videos[idx]['duration'] - \
                    transition_duration
                filters += (
                    f"[v{idx}]fade=t=out:st={accumulated_offset}:d={transition_duration}[v{idx+1}]; "
                )
            else:
                accumulated_offset += final_videos[idx -
                                                   1]['duration'] - transition_duration
                filters += (
                    f"[v{idx-1}][{idx}:v]xfade=transition=fade:duration={transition_duration}:offset={accumulated_offset}[v{idx}]; "
                )

    filters = filters.rstrip("; ")
    pr_name = pr_name.replace(" ", "_")
    pr_name = re.sub(r'[()\[\]{}]', '', pr_name)
    output_file = f"{pr_name}.mp4" if not webm else f"{pr_name}.webm"

    command = (
        f"{local_binary_folder}ffmpeg {verbose} -threads {threads} {inputs} -i {audio_file} -filter_complex \"{filters}\" "
        f"-map_metadata -1 -avoid_negative_ts make_zero -map \"[v{len(final_videos)}]\" -map {len(final_videos)}:a -c:a {audio_encoder} -b:a 320k -c:v {encoder} {quality} -video_track_timescale 24000 {output_file}"
    )

    print(command)
    os.system(command)

    print(f"Output file created: {output_file}")


def new_video_editing(pr_name: str, songs, threads=1, gpu=False, skip_preprocessing=False, skip_video_concatenation=False, skip_audio_concatenation=False, cpu_final=False, webm=False, fhd=False, local_binary_folder="", verbose=False):
    if not os.path.exists('temp'):
        os.makedirs('temp')
        
    if fhd:
        global width, height
        width = 1920
        height = 1080
    
    if verbose:
        verbose = "-v 40"
    else:
        verbose = ""

    encoder = "libx264"
    quality = "-crf 18"
    audio_encoder = "aac"
    if gpu:
        gpu_type = get_gpu_type()

        if gpu_type == "nvidia":
            print("Nvidia GPU detected")
            encoder = "h264_nvenc"
            quality = "-preset p5 -cq 20 -b:v 0"
        elif gpu_type == "amd":
            print("AMD GPU detected")
            encoder = "h264_amf"
            quality = "-qp 18"
        elif gpu_type == "intel":
            print("Intel GPU detected")
            encoder = "h264_qsv"
            quality = "-cq 18"
        else:
            print("No GPU detected")
            encoder = "libx264"
            quality = "-crf 18"

    start = time.time()

    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    #download(songs)

    if not verify_sample(songs, local_binary_folder):
        print("Sample duration exceeds video duration")
        exit(1)

    files: List[FileInfo] = []
    if not skip_preprocessing:
        files = preprocess_videos(songs, encoder, quality, threads, local_binary_folder, verbose)
    else:
        files, status = verify_preprocess_files(songs, local_binary_folder)
        if not status:
            print("Preprocessing files missing")
            exit(1)

    print(files)

    if not skip_video_concatenation:
        group_size = 8
        final_videos: List[FileInfo] = []

        for i in range(0, len(files), group_size):
            part_files = files[i:i + group_size]
            final_videos.append(concatenate_videos(
                part_files, i // group_size + 1, threads, encoder, quality, local_binary_folder, verbose))
    else:
        final_videos = verify_part_files(local_binary_folder)

    if not skip_audio_concatenation:
        final_audio = concatenate_audio(files, threads, local_binary_folder, verbose)
    else:
        if not os.path.exists("output_audio.wav"):
            print("Audio file missing")
            raise Exception("Audio file missing")
        final_audio = "output_audio.wav"
        
    if cpu_final:
        encoder = "libx264"
        quality = "-crf 18"
    elif webm:
        encoder = "libvpx-vp9"
        quality = "-b:v 4.5M"
        audio_encoder = "libopus"

    final_concatenate(pr_name, final_videos, final_audio, local_binary_folder, threads, encoder, quality, audio_encoder, webm, verbose)

    end = time.time()

    print(f"Total time: {end - start} seconds")

    return True
