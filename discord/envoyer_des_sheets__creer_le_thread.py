import discord
from discord.ext import commands
import asyncio
import configparser


config = configparser.ConfigParser()
config.read('../config.txt')
cometebot_key = config["discordl"]["cometebot_key"]

#Données:

a_coller ="""

"""


pr_name = 'Younha' #Nom du PR
deadline = '<t:1710543599:F>' #Deadline du PR
hosth = 'Comète' #Pseudo de l'Host du PR
idh = '362650795289608193' #ID Discord de l'Host du PR
servern = 'Les Pâtissières' #Nom du Serveur où le PR est Host
serverid = '741045187236593764' #ID du Serveur où le PR est Host
salon_thread = '994263990953857034' #ID du Salon où le thread sera créé


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

ping_thread = ""
for identifiant in id_discord:
    ping_thread += '<@'+str(identifiant) + '>'
    ping_thread += '\n'

message_thread = f"""
Bonjour !
Les sheets pour {pr_name} ont été envoyées.

{ping_thread}
N'hésitez pas à ping <@{idh}> si vous n'avez pas reçu votre sheet, bon pr à vous.

Deadline : {deadline}
"""

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
    channel_thread_id = salon_thread
    channel_thread = bot.get_channel(int(channel_thread_id))
    if channel_thread:
        thread = await channel_thread.create_thread(name=pr_name, type=discord.ChannelType.private_thread)
        message_du_thread_a_epingler = await thread.send(message_thread)
        await message_du_thread_a_epingler.pin()
        await channel.send(f'Le thread a été créé sur {servern}')
    else:
        print(f"Salon avec l'ID {channel_id} introuvable.")
        await channel.send(f"Le thread n'a pas été créé sur {servern}")
    

    print("Ready!")

bot.run(cometebot_key)
