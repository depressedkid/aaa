import discord
from discord.ext import commands

import requests

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bitcoin(self, ctx):
        url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.json(content_type="application/javascript")
            await ctx.send(f"Bitcoin price is: ${response['bpi']['USD']['rate']}")

    @commands.command()
    async def donald(self, ctx, tag: str = None):
        async with ctx.channel.typing():
            if not tag:
                response = requests.get("https://api.tronalddump.io/random/quote")
            else:
                response = requests.get(
                    f"https://api.tronalddump.io/tag/{urllib.parse.quote_plus(tag.lower().strip())}")
            r = response.json()
            await ctx.send(f"**{r['value']}**")

def setup(client):
    client.add_cog(Fun(client))
