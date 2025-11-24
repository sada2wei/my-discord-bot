import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")  # Koyeb の Environment Variable に設定
NOTIFY_USER_ID = int(os.getenv("NOTIFY_USER_ID"))  # 自分の Discord ID

# Intents 設定
intents = discord.Intents.default()
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ユーザーごとの前回ステータス記録
last_status = {}

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}.")

@bot.event
async def on_presence_update(before: discord.Member, after: discord.Member):
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
