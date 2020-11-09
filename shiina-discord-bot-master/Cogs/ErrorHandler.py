import discord
from discord.ext import commands

import json
import random

with open("Data/Config.json") as configFile:
    config = json.load(configFile)
    PHOTO = config["PHOTO"]

def getColour():
    return random.randint(0, 0xffffff)

# only Discord error handling
class ErrorHandler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        embed = discord.Embed(title=" ", colour=getColour())
        embed.add_field(name="Error:", value=f"`{error}`")
        embed.set_thumbnail(url=PHOTO)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(ErrorHandler(client))
