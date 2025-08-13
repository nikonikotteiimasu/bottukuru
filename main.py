import os
import discord
from discord import app_commands

TOKEN = os.getenv("TOKEN")  # Herokuの環境変数から取得

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@tree.command(name="start", description="開始して5回 # test を送信します")
async def start_command(interaction: discord.Interaction):
    await interaction.response.send_message("送信開始します", ephemeral=True)
    for _ in range(5):
        await interaction.channel.send("# おぜうの集いへ今すぐ参加！ [参加url](https://discord.gg/ozetudo)")

@bot.event
async def on_ready():
    print(f"✅ ログイン成功: {bot.user}")
    await tree.sync()

bot.run(TOKEN)
