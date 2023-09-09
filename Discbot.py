import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix= '!',intents=intents)
intents.members = True

@client.event

async def on_ready():
    print("The Discord Bot is online")
    print("-----------------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am a Bot")


@client.command()
async def Status(ctx):
    await ctx.send("Currently in Early Alpha Devlopment Phase")

@client.command()
async def bye(ctx):
    await ctx.send("Goodbye")

@client.event
async def on_member_join(member):
    channel=client.get_channel(1091292044137349130)
    await channel.send("Hello")
client.run('MTE0OTk3MzE2MjQxOTgzMDc4NQ.G10Hh1.yadDMwIof6IuniGqzIo9LHR_CiieMAVOAASehc')

