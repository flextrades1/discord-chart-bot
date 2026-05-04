import discord
import os
import time

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

    if len(parts) > 1 and parts[1] == "W":
        timeframe = "W"

    if ticker.endswith("USD") and not ticker.startswith("$"):
        ticker = f"${ticker}"

    chart_url = (
        f"https://stockcharts.com/c-sc/sc?s={ticker}&p={timeframe}"
        f"&i=t375773&r={int(time.time())}"
    )

    title = "Weekly" if timeframe == "W" else "Daily"

    embed = discord.Embed(title=f"{ticker} Chart ({title})")
    embed.set_image(url=chart_url)

    awa
