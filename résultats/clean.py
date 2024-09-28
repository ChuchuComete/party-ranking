import os
import shutil

def clean():
    for file in os.listdir():
        if file.endswith('.txt'):
            os.remove(file)
            
    for file in os.listdir():
        if file.endswith('_Affinity.png'):
            os.remove(file)
    
    for file in os.listdir():
        if file.endswith('_stats.txt'):
            os.remove(file)
            
    for file in os.listdir():
        if file.endswith('.mp3'):
            os.remove(file)
    
    for file in os.listdir():
        if file.endswith('.mp4'):
            os.remove(file)      
    
    if 'temp' in os.listdir():
        shutil.rmtree('temp')
            
    if 'layoutPR.png' in os.listdir():
        os.remove('layoutPR.png')    
        
    if 'progress.json' in os.listdir():
        os.remove('progress.json')
    
    
if __name__ == '__main__':
    clean()
