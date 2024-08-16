import discord
from discord.ext import commands
import asyncio
import requests
import os
import configparser


config = configparser.ConfigParser()
config.read('../config.txt')
cometebot_key = config["discord"]["cometebot_key"]
pr_path = config["general"]["pr_path"]
results_path  = f"{pr_path}/Résultats"
#Données:


pr_name = 'Haruka Shimotsuki' #Nom du PR
servern = 'Les Pâtissières' #Nom du Serveur où le PR est Host
serverid = '741045187236593764' #ID du Serveur où le PR est Host
salon_thread = '994263990953857034' #ID du Salon où le thread a été créé

os.makedirs(f"{results_path}/{pr_name}/pr-avatars/", exist_ok=True)

#Programme
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.',intents=intents)

async def save_image(attachment, author):
    response = requests.get(attachment.url)
    if response.status_code == 200:
        with open(f"{results_path}/{pr_name}/pr-avatars/{author}.png", 'wb') as file:
            file.write(response.content)
        print(f"Saved {author}.png")
    else:
        print(f"Failed to download {author}.png")


@bot.event
async def on_ready():
    channel = bot.get_channel(1209186270455275552)
    channel_thread_id = salon_thread
    channel_thread = bot.get_channel(int(channel_thread_id))
    active_threads = channel_thread.threads
    pr_thread_id = ""
    for thread in active_threads:
        if thread.name == pr_name:
            pr_thread_id = thread.id
    if pr_thread_id == "":
        exit(f"Thread {pr_name} not found")
    else:
        thread = bot.get_channel(pr_thread_id)
    
        if thread is None or not isinstance(thread, discord.Thread):
            print("Thread not found or invalid thread ID.")
            exit()
        
        messages = []
        async for message in thread.history(limit=None):
            messages.append(message)
        pp_message_list = [msg for msg in messages if msg.content.lower().startswith("pp")]
        for message in pp_message_list:
            await save_image(message.attachments[0], message.author)
        
    await bot.close()

bot.run(cometebot_key)
