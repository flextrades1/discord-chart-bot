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

    # Only respond to "$$"
    if not message.content.lower().startswith("$$"):
        return

    parts = message.content[2:].strip().upper().split()

    if len(parts) == 0:
        return

    ticker = parts[0]

    # Default timeframe
    timeframe = "D"

    if len(parts) > 1:
        if parts[1] == "W":
            timeframe = "W"
        elif parts[1] == "M":
            timeframe = "M"

    # Crypto formatting (BTCUSD etc)
    if ticker.endswith("USD") and not ticker.startswith("$"):
        ticker = f"${ticker}"

    # Chart URL
    chart_url = f"https://stockcharts.com/c-sc/sc?s={ticker}&p={timeframe}&i=t375773&r=7200"

    if timeframe == "W":
        title = "Weekly"
    elif timeframe == "M":
        title = "Monthly"
    else:
        title = "Daily"

    embed = discord.Embed(title=f"{ticker} Chart ({title})")
    embed.set_image(url=chart_url)

    await message.channel.send(embed=embed)


client.run(TOKEN)
