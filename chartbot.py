import 'dotenv/config'
import { Client, GatewayIntentBits } from 'discord.js'

const client = new Client({
  intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent]
})

client.once('ready', () => {
  console.log(`Logged in as ${client.user.tag}`)
})

client.on('messageCreate', async (message) => {
  if (message.author.bot) return

  const content = message.content.trim()

  // MONTHLY — fill chart
  if (content.startsWith('$$$')) {
    const ticker = content.replace('$$$', '').trim().toUpperCase()
    if (!ticker) return

    const chart = `https://stockcharts.com/c-sc/sc?s=${ticker}&p=M&yr=0&mn=0&dy=0&i=t8023489382c&r=`
    message.channel.send(chart)
    return
  }

  // WEEKLY — 18 months
  if (content.startsWith('$$')) {
    const ticker = content.replace('$$', '').trim().toUpperCase()
    if (!ticker) return

    const chart = `https://stockcharts.com/c-sc/sc?s=${ticker}&p=W&yr=1&mn=6&dy=0&i=t8023489382c&r=`
    message.channel.send(chart)
    return
  }

  // DAILY — fill chart
  if (content.startsWith('$')) {
    const ticker = content.replace('$', '').trim().toUpperCase()
    if (!ticker) return

    const chart = `https://stockcharts.com/c-sc/sc?s=${ticker}&p=D&yr=0&mn=0&dy=0&i=t8023489382c&r=`
    message.channel.send(chart)
    return
  }
})

client.login(process.env.DISCORD_TOKEN)
