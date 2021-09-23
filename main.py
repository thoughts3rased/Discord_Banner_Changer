from asyncio.tasks import Task
from logging import error
import discord
import os
import random
from discord.ext import tasks, commands

TOKEN = input("Enter your Discord Bot token.")
guildID = input("Enter the ID of the guild which you'd like to automate banner switching")
PREFIX = '!'
INTENTS = discord.Intents.default()
bot = commands.Bot(command_prefix=PREFIX, intents=INTENTS)
bot.remove_command('help')

class Loops(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.rotateBanners.start()
    
    def cog_unload(self):
        self.rotateBanners.cancel()
    
    
    @tasks.loop(minutes = 15)
    async def rotateBanners(self):
        try:
            guild = bot.get_guild(358708716599508993)
            newBanner = open(os.getcwd()+"\\banners\\"+(random.choice(os.listdir(os.getcwd()+"\\banners"))), "rb")
            await guild.edit(banner = newBanner.read())
            newBanner.close()
        except Exception as e:
            print(e)
        except discord.errors.HTTPException as e:
            print(e)



@bot.event
async def on_ready():
    print("Ready. Logged in as: " + bot.user.name)
    bot.add_cog(Loops(bot))

bot.run(TOKEN)
