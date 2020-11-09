import discord
from discord.ext import commands
from discord.utils import get
from gtts import gTTS
import os

def createAudio(text, language, slowed):
    fname_prefix = "SayAudio"
    count = 1
    while fname_prefix + str(count) + ".mp3" in os.listdir("Data/Audio/"):
        count += 1
    fname = fname_prefix + str(count) + ".mp3"
    audio_file = gTTS(text=text, lang=language, slow=slowed)
    audio_file.save(f"Data/Audio/{fname}")
    return fname

def deleteAudio(filename):
    os.remove(f"Data/Audio/{filename}")

class Talk(commands.Cog):
    DEFAULT_LANGUAGE = "en"
    IS_SLOW = False

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def say(self, ctx, *, message):
        filename = createAudio(message, self.DEFAULT_LANGUAGE, self.IS_SLOW)
        voice_client = get(self.client.voice_clients, guild=ctx.guild)
        voice_client.play(discord.FFmpegPCMAudio(executable="C:/Users/janso/Documents/GitHub/DiscordBotV2/ffmpeg.exe", source=f"Data/Audio/{filename}"))

    @commands.command()
    async def normal(self, ctx):
        self.IS_SLOW = False
        await ctx.send("[-] Speaking normal")

    @commands.command()
    async def slow(self, ctx):
        self.IS_SLOW = True
        await ctx.send("[-] Speaking slow")

    @commands.command(aliases=["Language"])
    async def language(self, ctx, language):
        self.DEFAULT_LANGUAGE = language
        await ctx.send(f"[-] Language set to {language}")

def setup(client):
    client.add_cog(Talk(client))
