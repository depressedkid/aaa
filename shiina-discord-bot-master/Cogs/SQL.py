import discord
from discord.ext import commands

import sqlite3
from sqlite3 import Error

import os
from time import ctime

name = "Data"

class SQL(commands.Cog):
    def __init__(self, client):
        self.client = client

    def create(self):
            try:
                connect = sqlite3.connect("./Data/" + name + ".db")
                print(f"[{ctime()}] Connected")

                cursor  = connect.cursor()
                print(f"[{ctime()}] Cursor created")

                cursor.execute("""CREATE TABLE Messages(
                                userID INT,
                                message TEXT,
                                date INT
                                )""")
                                
                print(f"[{ctime()}] Table created")

                connect.commit()
                print(f"[{ctime()}] Update Commited")

                connect.close()
                print(f"[{ctime()}] Connection closed\n")

            except Error as error:
                print(f"\n[{ctime()}] Error: {error}\n")

    def insert(self, message):
        try:
            connect = sqlite3.connect("./Data/" + name + ".db")
            cursor  = connect.cursor()

            cursor.execute("INSERT INTO Messages (userID, message, date) VALUES (?, ?, ?)", (message.author.id, message.content, message.created_at))
            print(f"[{ctime()}] Data Inserted Author ID: {message.author.id}, Message: {message.content}, Date: {message.created_at}")

            connect.commit()
            connect.close()

        except Error as error:
            print(f"[{ctime()}] Error: {error}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.client.user.id:
            return

        # Add file check
        self.insert(message)

    @commands.Cog.listener()
    async def on_ready(self):
        self.create()

def setup(client):
    client.add_cog(SQL(client))
