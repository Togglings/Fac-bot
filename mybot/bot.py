import traceback
import datetime
import discord
from discord.ext import commands
import sys

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    x = datetime.datetime.now()
    print(str(x) + "Logged in as", bot.user)
    print("\n")
    await bot.change_presence(activity=discord.Game("with yo walls nig"))

internal_extensions = ["cogs.advertiser"]

if __name__ == "__main__":
    for extension in internal_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"failed to load extension{extension}", file=sys.stderr)
            traceback.print_exc(e)

bot.run("NjQwMzExMjU1OTQ0NjU4OTU1.XeKYCg.yakqD0lX0YFvHs_4HXksv5UDm5k")
