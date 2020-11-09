import json

import discord
from discord.ext import commands

import random

def getColour():
    return random.randint(0, 0xffffff)

class About(commands.Cog):
    conf = {}

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def about(self, ctx):
        version = "1.0"
        owner = "583985397441232897"
        owner = await self.bot.fetch_user(owner)

        total_users = len(self.bot.users)

        channels: int = 0
        for guild in self.bot.guilds:
            channels += len(guild.channels)

        site = '[Documentation](https://yumenetwork.net)'
        server = '[Discord](https://yumenetwork.net/yumebot/invite/)'
        lib = '[Discord.py](https://github.com/Rapptz/discord.py/tree/rewrite)'

        embed = discord.Embed(
            title="About",
            colour=getColour(),
        )
        embed.set_footer(text=f"Shinaa {version} | By {owner}",
                         icon_url=owner.avatar_url)

        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name="Author", value="Name : {}#{}\n ID: {}".format(
            owner.name, owner.discriminator, owner.id), inline=True)
        embed.add_field(
            name="Stats",
            value=f"Guilds: {len(self.bot.guilds)}\nChannels: {channels} "
                  f"\nUsers: {total_users}",
            inline=True)

        embed.add_field(
            name="Informations",
            value=f"Version: {version} \nSite : {site} \nSupport : {server} \nLib : {lib}")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(About(bot))
