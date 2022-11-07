#import package

import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

#api-token
bot_token = os.getenv('token')
bot_prefix = os.getenv('prefix')

#prefix

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix= bot_prefix,intents=intents)


#LOGIN STATUS
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Streaming(name='step mom.jav', url='www.kontol.com'))
    print(f'Bot Name    :  {bot.user}')
    print(f'Aplication ID   :  {bot.application_id}')
    print(f'Latency   :  {bot.latency}')
    print(f'Status  :  {bot.status}')

@bot.command(help = "hai")
async def build(ctx):
    text = "Hallo"
    await ctx.send(text)

bot.run(bot_token)
