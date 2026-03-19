import discord
import os

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

    # Weekly option
    if len(parts) > 1 and parts[1] == "W":
        timeframe = "W"

    # Crypto formatting
    if ticker.endswith("USD") and not ticker.startswith("$"):
        ticker = f"${ticker}"

    # If no exchange specified, default to NYSE
    if ":" not in ticker and not ticker.startswith("$"):
        ticker = f"{ticker}:NYSE"

    chart_url = f"https://stockcharts.com/c-sc/sc?s={ticker}&p={timeframe}&i=t375773&r=7200"

    if timeframe == "W":
        title = "Weekly"
    else:
        title = "Daily"

    embed = discord.Embed(title=f"{ticker} Chart ({title})")
    embed.set_image(url=chart_url)

    await message.channel.send(embed=embed)


client.run(TOKEN)
