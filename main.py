import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='`')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(490477998395359242)
    await channel.send(f'{member} join!')

bot.run('NTk4OTAwNzI0MTE3Nzk4OTQ3.XUA7Ew.ivi6wrEyxCvjHZoyKUduzh2lB8Y')