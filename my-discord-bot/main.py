import discord
from discord.ext import commands

TOKEN = "あなたのBotトークン"
NOTIFY_USER_ID = 123456789012345678  # あなたのDiscordユーザーID

intents = discord.Intents.default()
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# 同じユーザーに何度も通知しないための記録
last_status = {}


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.event
async def on_presence_update(before: discord.Member, after: discord.Member):
    user_id = after.id

    # Bot自身は無視
    if after.bot:
        return

    new_status = str(after.status)

    # 前回ステータスと同じなら通知しない
    if last_status.get(user_id) == new_status:
        return

    last_status[user_id] = new_status

    # online のみ通知したい場合
    if new_status == "online":
        notify_user = await bot.fetch_user(NOTIFY_USER_ID)
        await notify_user.send(f"🔔 {after.name} がオンラインになりました！")


bot.run(TOKEN)
