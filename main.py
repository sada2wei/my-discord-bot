import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")
NOTIFY_USER_ID = int(os.getenv("NOTIFY_USER_ID"))

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
        return  # Botのステータスは無視

    user_id = after.id
    new_status = str(after.status)

    # 前回と同じステータスなら通知しない
    if last_status.get(user_id) == new_status:
        return

    last_status[user_id] = new_status

    # online になったときのみ自分のDMに通知
    if new_status == "online":
        try:
            notify_user = await bot.fetch_user(NOTIFY_USER_ID)
            await notify_user.send(f"🔔 {after.name} がオンラインになりました！")
        except discord.Forbidden:
            print(f"DM が送れませんでした: {NOTIFY_USER_ID}")
        except Exception as e:
            print(f"通知中にエラー発生: {e}")

bot.run(TOKEN)
