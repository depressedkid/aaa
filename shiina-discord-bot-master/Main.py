import discord
from discord.ext import commands

import os
import json
import time

from time import ctime

with open("Data/Config.json") as configFile:
    config = json.load(configFile)
    TOKEN = config["TOKEN"]
    PREFIX = config["PREFIX"]

client = commands.Bot(command_prefix=PREFIX)

for filename in os.listdir("./Cogs"):
    if filename.endswith(".py"):
        try:
            client.load_extension(f"Cogs.{filename[:-3]}")
        except discord.ext.commands.errors.ExtensionNotFound:
            print(f"[{ctime()}] {filename} extension not found")
        else:
            print(f"[{ctime()}] Loaded {filename}")

@client.event
async def on_ready():
    print(f"\n[{ctime()}] Username: {client.user.name}")
    print(f"[{ctime()}] ID:{client.user.id}")
    print(f"[{ctime()}] Version: {discord.__version__}\n")
    await client.change_presence(activity=discord.Streaming(name="center", url="https://www.youtube.com/watch?v=ub82Xb1C8os"))

if __name__ == "__main__":
    client.run(TOKEN)
