import discord 
import time
import json
from discord.ext import commands
import os
import asyncio

class Client(discord.Client):
    async def on_ready(self):
        print(f"helo it mi {self.user}")


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)  # running bot by parsing in the intents, and the functions are able to access intents
client.run("MTMyNTUxNzM2NjU0MDYzNjIwNA.GlEpmp.Q-T8G7Xi9XYHmKcd-ckt417tTLkgID0Q9Icw0Q") # unique token