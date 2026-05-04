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
    timeframe = "d"

    if len(parts) > 1 and parts[1].upper() == "W":
        timeframe = "w"

    chart_url = f"https://finviz.com/chart.ashx?t={ticker}&ty=c&ta=1&p={timeframe}&r={int(time.time())}"

    title = "Weekly" if timeframe == "w" else "Daily"

    embed = discord.Embed(title=f"{ticker} Chart ({title})")
    embed.set_image(url=chart_url)

    await message.channel.send(embed=embed)

client.run(TOKEN)
