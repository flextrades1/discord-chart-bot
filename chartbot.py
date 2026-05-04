import discord
import os
import time
import aiohttp

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot is online!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if not message.content.startswith("$$"):
        return

    parts = message.content[2:].strip().upper().split()
    if len(parts) == 0:
        return

    ticker = parts[0]
    timeframe = "D"

    if len(parts) > 1 and parts[1].upper() == "W":
        timeframe = "W"

    chart_url = (
        f"https://stockcharts.com/c-sc/sc?s={ticker}&p={timeframe}"
        f"&i=t375773&r={int(time.time())}"
    )

    headers = {
        "Referer": "https://stockcharts.com/",
        "User-Agent": "Mozilla/5.0"
    }

    title = "Weekly" if timeframe == "W" else "Daily"

    async with aiohttp.ClientSession() as session:
        async wi
