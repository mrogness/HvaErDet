# This example requires the 'message_content' intent.
import discord

# IMPORT THE OS MODULE.
import os

# translate
import asyncio
from googletrans import Translator

intents = discord.Intents.default()
intents.message_content = True

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.content.startswith("$nt"):
        m = message.content[3:]
        await message.channel.send((await Translator().translate(m, src="no")).text)

    if message.reference and message.content.startswith("$rnt"):
        m = (await message.channel.fetch_message(message.reference.message_id)).content
        await message.channel.send((await Translator().translate(m, src="no")).text)


client.run(DISCORD_TOKEN)
