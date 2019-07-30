import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='`')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('NTk4OTAwNzI0MTE3Nzk4OTQ3.XT_-IA.LxmblmpzsXkLj_UHyNk5RVUi3C8')

