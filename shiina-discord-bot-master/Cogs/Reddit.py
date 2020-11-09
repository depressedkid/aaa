import discord
from discord.ext import commands

import praw
import json
import random

reddit = praw.Reddit(client_id="2Z8hwp0EVd0_vQ", client_secret="eJdhbSuqx2iTuVidz1FeADXEV-Y", user_agent="Pink_Guy (by /u/Som_S_Som")

def getColour():
    return random.randint(0, 0xffffff)

#add NSFW channel check
class Reddit(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["NSFW"])
    async def nsfw(self, ctx):
        url = reddit.subreddit("nsfw").random().url

        embed = discord.Embed(title="nsfw", colour=getColour())
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["Meme"])
    async def meme(self, ctx):
        url = reddit.subreddit("me_irl").random().url

        embed = discord.Embed(title="Me IRL", colour=getColour())
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["Space"])
    async def space(self, ctx):
        url = reddit.subreddit("spaceporn").random().url

        embed = discord.Embed(title="Space", colour=getColour())
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["Pug"])
    async def pug(self, ctx):
        url = reddit.subreddit("pug").random().url

        embed = discord.Embed(title="Pug", colour=getColour())
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['chat'])
    @commands.guild_only()
    async def cat(self, ctx):
        r = requests.get('https://nekos.life/api/v2/img/meow')
        r = r.json()
        await ctx.send(r["url"])

    @commands.command()
    @commands.guild_only()
    async def dog(self, ctx):
        r = requests.get('https://random.dog/woof.json')
        r = r.json()
        await ctx.send(r["url"])
def setup(client):
    client.add_cog(Reddit(client))
