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

    if message.content.startswith("$$"):

        parts = message.content.replace("$$", "").strip().upper().split()
        ticker = parts[0]

        timeframe = "d"

        if len(parts) > 1:
            if parts[1] == "W":
                timeframe = "w"
            elif parts[1] == "M":
                timeframe = "m"

        # Auto-format crypto
        if ticker.endswith("USD") and not ticker.startswith("$"):
            ticker = f"${ticker}"

        if timeframe == "d":
            chart_url = f"https://stockcharts.com/c-sc/sc?s={ticker}&p=d&i=t375773&r=7200"
            title = "Daily"

        elif timeframe == "w":
            chart_url = f"https://stockcharts.com/c-sc/sc?s={ticker}&p=w&yr=2&i=t375773&r=7200"
            title = "Weekly"

        else:
            chart_url = f"https://stockcharts.com/c-sc/sc?s={ticker}&p=m&i=t375773&r=7200"
            title = "Monthly"

        embed = discord.Embed(title=f"{ticker} Chart ({title})")
        embed.set_image(url=chart_url)

        await message.channel.send(embed=embed)


client.run(TOKEN)
