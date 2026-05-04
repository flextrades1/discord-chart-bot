import discord
import os
import aiohttp
import io
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

    if len(parts) > 1:
        if parts[1] == "W":
            timeframe = "W"
        elif parts[1] == "M":
            timeframe = "M"

    # crypto formatting
    if ticker.endswith("USD") and not ticker.startswith("$"):
        ticker = f"${ticker}"

    if timeframe == "W":
        title = "Weekly"
    elif timeframe == "M":
        title = "Monthly"
    else:
        title = "Daily"

    # retry logic (THIS is what fixes your issue)
    for attempt in range(3):
        chart_url = f"https://stockcharts.com/c-sc/sc?s={ticker}&p={timeframe}&i=t375773&r={time.time()}"

        async with aiohttp.ClientSession() as session:
            async with session.get(chart_url) as resp:
                if resp.status == 200:
                    data = await resp.read()

                    file = discord.File(io.BytesIO(data), filename="chart.png")
                    embed = discord.Embed(title=f"{ticker} Chart ({title})")
                    embed.set_image(url="attachment://chart.png")

                    await message.channel.send(file=file, embed=embed)
                    return

        await asyncio.sleep(0.5)

    await message.channel.send(f"Failed to load chart for {ticker}. Try again.")


client.run(TOKEN)
