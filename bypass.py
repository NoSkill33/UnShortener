import discord
import datetime
from discord.ext import commands
import requests

bot      = commands.Bot(command_prefix='o!', description=" ")
intents  = discord.Intents().all()

@bot.command()
async def bypass(ctx, arg):
  r=requests.get('https://bypass.bot.nu/bypass2?url='+arg)
  a = ('%'+r.text)
  chunks = a.split(',')
  dest = chunks[1]
  stripped = dest.split('"')
  embed = discord.Embed()
  embed.add_field(name="Link:", value=stripped[3], inline=False)
  await ctx.send(embed=embed)
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('https://github.com/NoSkill33'))
    print('Logged in')

bot.run("enter token here")
