#usr/bin/env python3
'''
Name: HvaErDet?
Author: Matthew Rogness

Description:
A simple Discord bot that translates Norwegian text to English using the googletrans library.
The bot listens for messages starting with "$nt" to translate the following text, and messages starting
with "$rnt" to translate the content of the referenced message.
'''


import os
import discord
from googletrans import Translator
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True


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


def main():
    if not DISCORD_TOKEN:
        raise SystemExit("DISCORD_TOKEN is not set. Add it to your environment or .env file.")
    client.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
