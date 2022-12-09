""" 
    ! README !
    Sh#t no one reads.

    ! SUMMARY !
    This is a demo of OpenAI's GPT-3 API. 
    It's a Discord bot that uses OpenAI's API to generate text based on a prompt.

    ! HOW TO USE !
    1. Create a Discord bot and invite it to your server.
    2. Create a .env file in the same directory as this file.
    3. Add your OpenAI API key and Discord bot token to the .env file.
    4. Run this file.

"""

import os
import openai # pip install openai
import discord # pip install discord.py
from discord import app_commands
from dotenv import load_dotenv # pip install python-dotenv
from typing import Optional
load_dotenv()

# Load environment variables since.. like, I don't plan to get my token stolen. lol.
# If you clone this, be sure to make your own .env file.

# With the following: 
# OPENAI_TOKEN
# OPENAI_ENGINE
# DISCORD_TOKEN
# DISCORD_GUILD

OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')
OPENAI_ENGINE = os.getenv('OPENAI_ENGINE')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD = int(os.getenv('DISCORD_GUILD'))

openai.api_key = OPENAI_TOKEN

client = discord.Client(intents=discord.Intents.default())
tree = app_commands.CommandTree(client)

@tree.command(name="generate", description="Generates a response to your prompt using the OpenAI API.", guild=discord.Object(id=DISCORD_GUILD))
async def generate(ctx: discord.Interaction, prompt: str, engine: Optional[str] = OPENAI_ENGINE):
    try:
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=1024,
            temperature=1,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        await ctx.response.send_message(response["choices"][0]["text"])
        
    except Exception as e:
        await ctx.response.send_message(f"An error occured: {e}")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=DISCORD_GUILD))

client.run(DISCORD_TOKEN)
