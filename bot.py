import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="//")


@bot.event
async def on_ready():
    print("Femboy mode activated, owo.")
    """simple commands"""

@bot.command()
async def info(ctx):
    await ctx.send("Hi owo, my name is Dylan and I am the official bot of Atwol's Discord server!")

@bot.command()   
async def ping(ctx):
    await ctx.send("Pong")

@bot.command() 
async def creator(ctx):
    await ctx.send("Crin is my creator and she is very pogger, owo")           

    
    

bot.run("token")
