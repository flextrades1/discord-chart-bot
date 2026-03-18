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

        ticker = message.content.replace("$$", "").strip().upper()

        # Handle crypto automatically
        if ticker.endswith("USD") and not ticker.startswith("$"):
            ticker = f"${ticker}"

        chart_url = f"https://stockcharts.com/c-sc/sc?s={ticker}&p=D&yr=0&mn=6&dy=0&i=t375773&r=5000"

        embed = discord.Embed(title=f"{ticker} Chart")
        embed.set_image(url=chart_url)

        await message.channel.send(embed=embed)


client.run(TOKEN)
