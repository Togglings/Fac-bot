import discord
from discord.ext import commands, tasks
import asyncio
import datetime
from time import sleep

class AdvertisementCog(commands.Cog, name = "Advertisement"):

    def __init__(self, bot):
        self.bot

    @commands.command()
    async def ping(self, cxt):
        await cxt.send("pong")

def setup(bot):
    bot.add_cog(AdvertisementCog(bot))
    print("AdvertisementCog is loaded")
