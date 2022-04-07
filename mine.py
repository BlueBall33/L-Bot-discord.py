import os
import random

import nextcord as discord
from nextcord.ext import commands, tasks

#======# CONFIG #======#

Tocken = ""
Prefix = ""
statusy = [
    f'{Prefix}pomoc',
    'Redy'
]

#=======================#

client = commands.Bot(command_prefix=Prefix, case_insensitive=True)
client.remove_command("help")
client.members = True



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



@tasks.loop(seconds=10)
async def status():
    await client.change_presence(activity=discord.Game(name=statusy[random.randint(0, len(statusy))-1]))



@client.event
async def on_ready():
    print('Bot Redy')
    status.start()




client.run(Tocken)
