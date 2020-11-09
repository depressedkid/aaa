import discord
from discord.ext import commands

import json
import os

from time import ctime

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def updateData(self, users, user):
        if not f"{user.id}" in users:
            users[f"{user.id}"] = {}
            users[f"{user.id}"]['experience'] = 0
            users[f"{user.id}"]['level'] = 1

    async def addExperience(self, users, user, exp):
        users[f"{user.id}"]["experience"] += exp

    async def levelUp(levelUp, users, user, message):
        experience = users[f"{user.id}"]["experience"]
        lvlStart = users[f"{user.id}"]["level"]
        lvlEnd = int(experience ** (1 / 4))
        if lvlStart < lvlEnd:
            await message.channel.send(f"[ - ] {user.mention} has leveled up to `{lvlEnd}`")
            users[f"{user.id}"]["level"] = lvlEnd

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        firstChannel = guild.text_channels[0]
        await firstChannel.send("code that thinks")

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            with open("Data/Score.json", "r") as scoreFile:
                users = json.load(scoreFile)

            await self.updateData(users, message.author)
            await self.addExperience(users, message.author, 0.5)
            await self.levelUp(users, message.author, message)

            with open('Data/Score.json', 'w') as scoreFile:
                json.dump(users, scoreFile)

            await self.updateData(users, message.author)
            await self.addExperience(users, message.author, 0.5)
            await self.levelUp(users, message.author, message)

            with open("Data/Score.json", "w") as scoreFile:
                json.dump(users, scoreFile)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not message.author.bot:
            author  = message.author
            content = message.content
            channel = message.channel
            print(f"[{ctime()}]{author} Deleted: {content}")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open("Data/score.json", "r") as scoreFile:
            users = json.load(scoreFile)

        await self.updateData(users, member)

        with open("data/score.json", "w") as scoreFile:
            json.dump(users, scoreFile)

        await member.create_dm()
        await member.dm_channel.send(f"[ - ] `Welcome to Anti social kids Discord server. Server website: http://antisocialkids.wtf/`")

def setup(client):
    client.add_cog(Events(client))
