
import discord
import os

client = discord.Client()

class chatbot(discord.Client):
    async def on_ready(self):
        game = discord.Game("<+명령어> for help")
        await client.change_presence(status=discord.Status.idle, activity=game)
        
    async def on_message(self, message):
        if message.author.bot:
            return None


if __name__ == "__main__":
    client = chatbot()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author not in users:
        users[message.author] = {}

    if message.content.startswith("+방송"):
        embed = discord.Embed(title="방송 예정표", description="시간과 내용이 변경될 수 있습니다", color=0x00ffff)
        embed.set_author(name="방송")
        embed.add_field(name="현재 진행중인 방송", value="WNN 10시 뉴스 진행중", inline=False)
        embed.add_field(name="다음 방송", value="WNN 현충일 특별편 진행 예정", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/786048037184208946/850728577992228934/-.-001.jpg")
        embed.set_footer(text="Friend community team")
        await message.channel.send(embed=embed)

access_token = os.environ['BOT_TOKEN']
client.run('access_token')
