import discord
from discord.ext import commands
import googlesearch
import urllib.request
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import wikipedia
import aiohttp
from io import BytesIO

import asyncio
import PIL

async def process_url(ctx, argument):
    if argument is None:
        is_found = False
        for att in ctx.message.attachments:
            if att.height is not None and not is_found:
                url = att.proxy_url
                is_found = True
        if not is_found:
            url = str(ctx.author.avatar_url_as(format="png", size=1024))
    else:
        try:
            url = str(
                (await commands.MemberConverter().convert(ctx, argument)).avatar_url_as(
                    format="png", size=1024
                )
            )
        except commands.BadArgument:
            try:
                url = str(
                    (
                        await commands.UserConverter().convert(ctx, argument)
                    ).avatar_url_as(format="png", size=1024)
                )
            except commands.BadArgument:
                url = argument

    try:
        async with ctx.bot.http2.get(url) as resp:
            try:
                img = PIL.Image.open(BytesIO(await resp.content.read())).convert("RGB")
            except OSError:
                if ctx.command.qualified_name == "sort":
                    return  # error handler caught it
                else:
                    await ctx.send(":x: That URL is not an image.")
                    return
    except aiohttp.InvalidURL:
        if ctx.command.qualified_name == "sort":
            return  # error handler caught it
        else:
            await ctx.send(":x: That URL is invalid.")
            return

    return img

async def url_status_ok(url):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as resp:
            return resp.status != 404


class Web(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def google(self, ctx, *, query):
        """Searches Google"""

        def gsync(query=query):
            name = str(ctx.message.author)
            for j in search(query, tld="com", num=1, stop=1):
                print(f"{name} has searched for '{query}' and it returned {j}")
                return j

        async with ctx.typing():
            gasync = await self.client.loop.run_in_executor(ThreadPoolExecutor(), gsync)
            await ctx.send(gasync)

def setup(client):
    client.add_cog(Web(client))
