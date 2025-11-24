import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# .env を読み込む（Koyeb では環境変数を使うので.envは不要でもOK）
load_dotenv()

TOKEN = os.getenv("TOKEN")  # Koyeb の Environment Variable に設定
NOTIFY_USER_ID = int(os.getenv("NOTIFY_USER_ID"))  # あなたの Discord ID

# Intent 設定
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
    # Bot は無視
    if after.bot:
        return

    user_id = after.id
    new_status = str(after.status)

    # 前回と同じステータスなら無視
    if last_status.get(user_id) == new_status:
        return

    last_status[user_id] = new_status

    # onlineになった場合のみ通知
    if new_status == "online":
        notify_user = await bot.fetch_user(NOTIFY_USER_ID)
        await notify_user.send(f"🔔 {after.name} がオンラインになりました！")

bot.run(TOKEN)
