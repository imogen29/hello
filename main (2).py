import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

# 啟用意圖（包含訊息和成員事件）
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# 初始化機器人，設定指令前綴（這裡設為空字串，代表不用打 !）
bot = commands.Bot(command_prefix="", intents=intents)

# 當機器人啟動完成
@bot.event
async def on_ready():
    print(f"✅ 機器人已上線：{bot.user}")

# 當有新成員加入伺服器
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="welcome!")  # 這裡改成你實際的頻道名稱
    if channel:
        await channel.send(f"歡迎 {member.mention} 加入錚錚子的窩～快打聲招呼吧！")

# 當有訊息出現
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "哈囉":
        await message.channel.send("哈囉寶寶，歡迎來到錚錚子的窩!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
        
    if message.content == "願懷":
        answers = [
            "怎麼了小寶？",
            "小寶想我嗎？",
            "想你",
            "愛你",
            "想我就說"
        ]
        await message.channel.send(random.choice(answers))

    # 這行超重要，不然未來你如果用 @bot.command() 會壞掉
    await bot.process_commands(message)

bot.run("MTM5MDAwNDI4NTY1OTU0OTcxNg.GCzIeM.SYWbee7HIEw0C4dWJuV120lfxlsaI7vwn_jcks")
print(f"Token: {token}")  # 測試有沒有拿到token

bot.run(token)
