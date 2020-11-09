import discord
from discord.ext import commands
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw, ImageEnhance, ImageFilter, ImageOps
import textwrap
import numpy as np
import copy
import typing
import os
import asyncio
import functools
import aiohttp

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

loop = asyncio.get_event_loop()

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer

def link(arr, arr2):
    rgb1 = arr.reshape((arr.shape[0] * arr.shape[1], 3))
    rgb2 = list(map(tuple, arr2.reshape((arr2.shape[0] * arr2.shape[1], 3))))
    template1 = {x: [0, []] for x in rgb2}
    for x, y in zip(rgb2, rgb1):
        template1[x][1].append(y)
    return template1


def reset_template(template):
    for v in template.values():
        v[0] = 0


class Image_(commands.Cog, name="Image"):
    def __init__(self, client):
        self.client = client

    async def cog_before_invoke(self, ctx):
        if "cogs" in os.getcwd():
            os.chdir("..")

    @commands.command()
    async def kirby(self, ctx, *, sent: commands.clean_content):
        bio = BytesIO()
        image = Image.open(r"Data/Photos/birby.png")
        font = ImageFont.truetype("Data/Photos/ARIAL.TTF", 26)
        draw = ImageDraw.Draw(image)
        draw.text(
            xy=(100, 100),
            text="\n".join(textwrap.wrap(sent, width=25)),
            fill=(0, 0, 0),
            font=font,
        )
        image.save(bio, format="png")
        bio.seek(0)
        await ctx.send(file=discord.File(bio, "out.png"))

    @commands.command()
    async def lisa(self, ctx, *, sent: commands.clean_content):
        bio = BytesIO()
        image = Image.open(r"Data/Photos/lisa.png")
        font = ImageFont.truetype("Data/Photos/ARIAL.TTF", 26)
        draw = ImageDraw.Draw(image)
        draw.text(
            xy=(200, 100),
            text="\n".join(textwrap.wrap(sent, width=19)),
            fill=(0, 0, 0),
            font=font,
        )
        image.save(bio, format="png")
        bio.seek(0)
        await ctx.send(file=discord.File(bio, "out.png"))

    @commands.command(aliases=["pewdiepie", "felix"])
    async def pewds(self, ctx, *, sent: commands.clean_content):
        bio = BytesIO()
        image = Image.open(r"Data/Photos/pewds.jpg")
        font = ImageFont.truetype("Data/Photos/ARIAL.TTF", 18)
        draw = ImageDraw.Draw(image)
        draw.text(
            xy=(210, 50),
            text="\n".join(textwrap.wrap(sent, width=6)),
            fill=(0, 0, 0),
            font=font,
        )
        image.save(bio, format="png")
        bio.seek(0)
        await ctx.send(file=discord.File(bio, "out.png"))

    @commands.command()
    async def gru(self, ctx, *, sent: commands.clean_content):
        bio = BytesIO()
        image = Image.open(r"Data/Photos/gru.png")
        font = ImageFont.truetype("Data/Photos/ARIAL.TTF", 18)
        draw = ImageDraw.Draw(image)
        draw.text(
            xy=(180, 50),
            text="\n".join(textwrap.wrap(sent, width=10)),
            fill=(0, 0, 0),
            font=font,
        )
        image.save(bio, format="png")
        bio.seek(0)
        await ctx.send(file=discord.File(bio, "out.png"))

    @commands.command()
    async def linus(self, ctx, *, sent: commands.clean_content):
        bio = BytesIO()
        image = Image.open(r"Data/Photos/linus.png")
        font = ImageFont.truetype("Data/Photos/ARIAL.TTF", 72)
        draw = ImageDraw.Draw(image)
        draw.text(
            xy=(575, 100),
            text="\n".join(textwrap.wrap(sent, width=15)),
            fill=(0, 0, 0),
            font=font,
        )
        image.save(bio, format="png")
        bio.seek(0)
        await ctx.send(file=discord.File(bio, "out.png"))

    @commands.command()
    async def trump(self, ctx, *, sent: commands.clean_content):
        bio = BytesIO()
        image = Image.open(r"Data/Photos/frump.jpg")
        font = ImageFont.truetype("Data/Photos/ARIAL.TTF", 26)
        draw = ImageDraw.Draw(image)
        draw.text(
            xy=(375, 300),
            text="\n".join(textwrap.wrap(sent, width=16)),
            fill=(0, 0, 0),
            font=font,
        )
        image.save(bio, format="png")
        bio.seek(0)
        await ctx.send(file=discord.File(bio, "out.png"))

    @commands.command()
    async def elon(self, ctx, *, sent: commands.clean_content):
        bio = BytesIO()
        image = Image.open(r"Data/Photos/elonian.png")
        font = ImageFont.truetype("Data/Photos/ARIAL.TTF", 26)
        draw = ImageDraw.Draw(image)
        draw.text(
            xy=(225, 100),
            text="\n".join(textwrap.wrap(sent, width=11)),
            fill=(0, 0, 0),
            font=font,
        )
        image.save(bio, format="png")
        bio.seek(0)
        await ctx.send(file=discord.File(bio, "out.png"))

    @commands.command(aliases=["sponge", "bob"])
    async def spongebob(self, ctx, *, sent: commands.clean_content):
        bio = BytesIO()
        image = Image.open(r"Data/Photos/spongboi.png")
        font = ImageFont.truetype("Data/Photos/ARIAL.TTF", 92)
        draw = ImageDraw.Draw(image)
        draw.text(
            xy=(710, 95),
            text="\n".join(textwrap.wrap(sent, width=10)),
            fill=(0, 0, 0),
            font=font,
        )
        image.save(bio, format="png")
        bio.seek(0)
        await ctx.send(file=discord.File(bio, "out.png"))

    @commands.command(aliases=["board"])
    async def billboard(self, ctx, *, sent: commands.clean_content):
        bio = BytesIO()
        image = Image.open(r"Data/Photos/billboard.jpg")
        font = ImageFont.truetype("Data/Photos/ARIAL.TTF", 26)
        draw = ImageDraw.Draw(image)
        draw.text(
            xy=(30, 75),
            text="\n".join(textwrap.wrap(sent, width=32)),
            fill=(0, 0, 0),
            font=font,
        )
        image.save(bio, format="png")
        bio.seek(0)
        await ctx.send(file=discord.File(bio, "out.png"))

def setup(client):
    client.add_cog(Image_(client))
