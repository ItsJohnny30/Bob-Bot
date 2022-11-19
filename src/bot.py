'''
     ██╗ ██████╗ ██╗  ██╗███╗   ██╗███╗   ██╗██╗   ██╗██╗    ██╗ █████╗ ██╗  ██╗██████╗ ██████╗ ██╗  ██╗███████╗
     ██║██╔═══██╗██║  ██║████╗  ██║████╗  ██║╚██╗ ██╔╝██║    ██║██╔══██╗██║ ███║╚════██╗╚════██╗██║  ██║██╔════╝
     ██║██║   ██║███████║██╔██╗ ██║██╔██╗ ██║ ╚████╔╝ ██║ █╗ ██║███████║██║ ╚██║ █████╔╝ █████╔╝███████║███████╗
██   ██║██║   ██║██╔══██║██║╚██╗██║██║╚██╗██║  ╚██╔╝  ██║███╗██║██╔══██║██║  ██║██╔═══╝  ╚═══██╗╚════██║╚════██║
╚█████╔╝╚██████╔╝██║  ██║██║ ╚████║██║ ╚████║   ██║   ╚███╔███╔╝██║  ██║██║  ██║███████╗██████╔╝     ██║███████║
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝   ╚═╝    ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝      ╚═╝╚══════╝                                                                                              
 '''                   
                                                                                                                                                                                        
import discord
from discord.ext import commands
import json
import random

with open('config.json', 'r', encoding="utf8") as config:
  config = json.load(config)

bot = commands.Bot(command_prefix= config["Prefix"], intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(">> Bot is Online <<")
    print(f"-- Login From: {bot.user}")
    print("This Bot Make By Johnnywai12345")

@bot.command()
async def bob(ctx):
    await ctx.reply("POP!!! Im a Bob Bot!!!!!!!")

bot.remove_command("help")
@bot.command()
async def help(ctx):
    await ctx.reply("Help - Center\n\n\nMain: bob, ping\nOther: invite, tandas")

@bot.command()
async def ping(ctx):
    await ctx.reply(f'Pong! {round(bot.latency*1000)} ms')

@bot.command()
async def invite(ctx):
    await ctx.reply(config["Invite_Link"])

@bot.command()
async def tandas(ctx):
    pic = random.choice(["https://th.bing.com/th/id/OIP.GjytKemR9aYK4kSVV1eArwHaHa?pid=ImgDet&rs=1", "https://th.bing.com/th/id/R.ec6d4b460b599ba101b5080c13d10a87?rik=YeNjxRFIWphuow&riu=http%3a%2f%2flibreshot.com%2fwp-content%2fuploads%2f2016%2f07%2ftoilet.jpg&ehk=2sOu94ZsidU6ywweTWYF%2f9lbWAxipUnmLNllSCJWs9E%3d&risl=&pid=ImgRaw&r=0", "https://cdnassets.hw.net/cb/75/61ad1f1c4ade83627dfcce1fb2e9/tmp75b-2etmp-tcm20-187135.jpg", "https://www.signaturehardware.com/media/catalog/product/5/2/524069-one-piece-toilet-white_1.jpg"])

    await ctx.reply(pic)


bot.run(config["Token"])