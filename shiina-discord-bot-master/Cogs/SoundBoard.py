import discord
from discord.ext import commands

import asyncio
from discord.utils import get

class SoundBoard(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def playFile(self, ctx, filename):
        if not ctx.author.voice:
            await ctx.send("[-] Join a Voice Channel")
            return

        source = discord.FFmpegPCMAudio(filename)
        voice_client = get(self.client.voice_clients, guild=ctx.guild)
        voice_client.play(source)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=["Oof"])
    async def oof(self, ctx):
        await self.playFile(ctx, "Sounds/Oof.mp3")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=["Countdown"])
    async def countdown(self, ctx):
        await self.playFile(ctx, "Sounds/CountDown.mp3")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=["Enthusiasm"])
    async def enthusiasm(self, ctx):
        await self.playFile(ctx, "Sounds/Enthusiasm.mp3")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=["DidntAsk"])
    async def didntask(self, ctx):
        await self.playFile(ctx, "Sounds/DidntAsk.mp3")

def setup(client):
    client.add_cog(SoundBoard(client))
