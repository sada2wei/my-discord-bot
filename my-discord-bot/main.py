import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")
NOTIFY_USER_ID = int(os.getenv("NOTIFY_USER_ID"))

intents = discord.Intents.default()
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

last_status = {}

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.event
async def on_presence_update(before, after):
    if after.bot:
        return

    user_id = after.id
    new_status = str(after.status)

    if last_status.get(user_id) == new_status:
        return

    last_status[user_id] = new_status

    if new_status == "online":
        notify_user = await bot.fetch_user(NOTIFY_USER_ID)
        await notify_user.send(f"🔔 {after.name} がオンラインになりました！")


bot.run(TOKEN)
