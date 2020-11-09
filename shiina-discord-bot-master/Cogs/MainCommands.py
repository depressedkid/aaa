import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

import json
import random

import os
import requests

with open("Data/Config.json") as configFile:
    config = json.load(configFile)
    username = config["USERNAME"]
    password = config["PASSWORD"]

class MainCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=["Ping"])
    async def ping(self, ctx):
        latency = round(self.client.latency, 2)
        await ctx.send(f"Pong! `{latency}s` response time")  # {client.latency}")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=["Invite"])
    async def invite(self, ctx):
        inviteLink = await ctx.channel.create_invite(max_uses=1, unique=True)
        await ctx.author.send(inviteLink)
        await ctx.send("Link created! `Check DM's`")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=["Password"])
    async def password(self, ctx):
        chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[]^_`{|}~'
        list = []
        length = 16

        for x in range(length):
            list.append(random.choice(chars))
        password = ''.join(list)

        await ctx.send(f"[ - ] Password generated! `Check DM's`")
        await ctx.author.send(f"Password: `{password}`")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=["Level"])
    async def level(self, ctx, member: discord.Member):
        with open('Data/Score.json', 'r') as scoreFile:
            users = json.load(scoreFile)
        level = users[f'{member.id}']['level']
        await ctx.send(f"[ - ] {member.mention} level is: `{level}`")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=["Pfp"])
    async def pfp(self, ctx, member: discord.Member):
        await ctx.send(member.avatar_url)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=["Duck"])
    async def duck(self, ctx, meme_id: int, *args):
        memes = requests.get(
            'https://api.imgflip.com/get_memes').json()['data']['memes']
        url = 'https://api.imgflip.com/caption_image'
        template_id = 0
        try:
            template_id = meme_id
        except ValueError:
            for meme in memes:
                if meme_id.casefold() in meme['name'].casefold():
                    template_id = meme['id']
                    break

        params = dict(
            template_id=template_id,
            username=username,
            password=password)
        for i, text in enumerate(args):
            params["text" + str(i)] = text
            res = requests.get(url, params=params)
            data = res.json()
        await ctx.send(data['data']['url'])

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=["Templates"])
    async def templates(self, ctx):
        await ctx.send(f"{ctx.author.mention} Templates: https://api.imgflip.com/popular_meme_ids", delete_after=60)

def setup(client):
    client.add_cog(MainCommands(client))
