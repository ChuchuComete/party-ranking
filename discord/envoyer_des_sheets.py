import discord
from discord.ext import commands
import asyncio
import configparser


config = configparser.ConfigParser()
config.read('../config.txt')
cometebot_key = config["discordl"]["cometebot_key"]

#Données:

a_coller ="""
Comète	362650795289608193	https://docs.google.com/spreadsheets/....
Comète	362650795289608193	https://docs.google.com/spreadsheets/....

"""


pr_name = 'Test' #Nom du PR
deadline = '''<t:1708124399:F>''' #Deadline du PR
hosth = 'Comète' #Pseudo de l'Host du PR
idh = '362650795289608193' #ID Discord de l'Host du PR
servern = 'Les Pâtissières' #Nom du Serveur où le PR est Host
serverid = '741045187236593764' #ID du Serveur où le PR est Host

#Programme

liste = a_coller.split()

id_discord = []
pseudo_discord = []
lien_sheet = []

for i in range(len(liste)):
    if i%3==1:
        id_discord.append(liste[i])
    elif i%3==0:
        pseudo_discord.append(liste[i])
    else:
        lien_sheet.append(liste[i])

print(id_discord)
print(pseudo_discord)
print(lien_sheet)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.',intents=intents)

async def send_sheet(pr, uid, name, sheet):
    print("send sheet")
    await asyncio.sleep(2)
    channel = bot.get_channel(1209186270455275552)
    await channel.send(f'Sending to {name} (<@{uid}>) du serveur {servern} pour le PR {pr}')
    guild = bot.get_guild(int(f'{serverid}'))
    msg = f'Hi {name}. This is an automated message so please don\'t reply to the bot :). If you wish to say anything, dm the PR host <@{idh}> ({hosth}) directly. Here\'s your **{pr}** sheet link, please be done by the deadline or earlier if possible: {sheet}\n Deadline: **{deadline}**'
    pl = guild.get_member(int(uid))
    try:
        await pl.send(msg)
    except Exception as ex:
        await channel.send(f'Exception at player {name} (<@{uid}>). | (Their sheet: {sheet}) Ex: + {ex}')

async def main():
    print('main')
    for i in range(len(pseudo_discord)):
        await send_sheet(pr_name, id_discord[i], pseudo_discord[i], lien_sheet[i])


@bot.event
async def on_ready():
    await main()
    channel = bot.get_channel(1209186270455275552)
    await channel.send('Terminé')

    print("Ready!")

bot.run('cometebot_key')

