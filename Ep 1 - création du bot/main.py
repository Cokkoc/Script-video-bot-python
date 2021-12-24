import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
	print("Je suis en ligne.")

bot.run("ODk2NDI3ODQyMzc4ODEzNTMw.YWG9fA.jEjDPO_ZoPdtgg7DgNECw9D6N3I")
