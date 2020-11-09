import discord
from discord.ext import commands

import json
import random

with open("Data/Config.json") as configFile:
    config = json.load(configFile)
    PHOTO = config["PHOTO"]

def getColour():
    return random.randint(0, 0xffffff)

class AdminCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["Logout"])
    async def logout(self, ctx):
        if ctx.author.guild_permissions.administrator:
            await ctx.send(f"[-] `{self.client.user.name}` has logged out")
            await self.client.logout()
            embed = discord.Embed(title=" ", description=" ", colour=getColour())
            embed.add_field(name="Logout", value=f"`{self.client.user.name}`")
            embed.set_thumbnail(url=BANPHOTO)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{ctx.author.mention} [-] No permissions")

    @commands.command(aliases=["Clear"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        channel = ctx.message.channel
        amountDeleted = 0
        messages = []

        async for message in channel.history(limit=amount):
            messages.append(message)
            amountDeleted = amountDeleted + 1
        await channel.delete_messages(messages)
        embed = discord.Embed(title=" ", description=" ", colour=getColour())
        embed.add_field(name="Deleted:", value=f"`{amountDeleted}`")
        embed.add_field(name="Channel", value=f"`{channel}`")
        embed.set_thumbnail(url=PHOTO)
        await ctx.send(embed=embed)

    @commands.command(aliases=["Kick"])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        await member.kick(reason=reason)
        embed = discord.Embed(title="Kick", description=" ", colour=getColour())
        embed.add_field(name="User", value=f"@{user.name}#{user.discriminator}")
        embed.add_field(name="Reason", value=f"{reason}")
        embed.set_thumbnail(url=BANPHOTO)
        await ctx.send(embed=embed)

    @commands.command(aliases=["Ban"])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason = None):
        await user.ban(reason=reason)
        embed = discord.Embed(title="Ban", description=f"{user.name} has been banned", colour=getColour())
        embed.add_field(name="User", value=f"@{user.name}#{user.discriminator}")
        embed.add_field(name="Reason", value=f"{reason}")
        embed.set_thumbnail(url=PHOTO)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(title="User Unbanned", description=" ", colour=getColour())

                embed.add_field(name="User", value=f"@{user.name}#{user.discriminator}")
                embed.set_thumbnail(url=PHOTO)
                await ctx.send(embed=embed)

def setup(client):
    client.add_cog(AdminCommands(client))
