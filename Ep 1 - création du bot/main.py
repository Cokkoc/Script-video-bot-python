import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "d!", description = "Bot de test")

@bot.event
async def on_ready():
    print("Le bot est lancé.")

bot.run("ODk2NDI3ODQyMzc4ODEzNTMw.YWG9fA.jEjDPO_ZoPdtgg7DgNECw9D6N3I")
