import discord
import datetime
from discord.ext import commands
import requests

##################################################################################################################
bot      = commands.Bot(command_prefix='o!', description=" ")
intents  = discord.Intents().all()

##################################################################################################################
@bot.command(   )
async def bypass(ctx, arg):
  r=requests.get('https://bypass.bot.nu/bypass2?url='+arg)
  a = ('%'+r.text)
  chunks = a.split(',')
  dest = chunks[1]
  stripped = dest.split('"')
  embed = discord.Embed()
  #embed.set_thumbnail(url="https://cdn.discordapp.com/icons/892738398278787083/b0c1804bf9ec517e5fd89485cb671c02.png?size=4096")
  embed.add_field(name="Bypassed:", value=stripped[3], inline=False)
  await ctx.send(embed=embed)
  print(f"{ctx.author} used bypass on ({arg}/{stripped[3]})")

##################################################################################################################
@bot.event
async def on_ready(  ):
    await bot.change_presence(activity=discord.Game('Omegus Bypass'))
    print('                 Logged in as:\n[>] {0.user.name}\n[>] {0.user.id}'.format(bot))


    print('                 Bot Is Ready')
bot.run("BOT TOKEN")
