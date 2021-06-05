
import discord
import os

client = discord.Client()

users = {}  

class chatbot(discord.Client):
    async def on_ready(self):
        game = discord.Game("<+명령어> for help")
        await client.change_presence(status=discord.Status.idle, activity=game)
        #idle = 자리비움
        #dnd(do_not_disturb) = 다른 용무 중
        #on.offline = 온.오프라인

    async def on_message(self, message):
        if message.author.bot:
            return None


if __name__ == "__main__":
    client = chatbot()

@client.event
async def on_message(message):
    global users
    prefix = "+"
    if message.author == client.user:
        return

    if message.author not in users:
        users[message.author] = {}

    if message.content.startswith(prefix + '명령어'):
        embed = discord.Embed(title="+명령어를 쳐서 명령어를 알아 볼 수 있어요", description="몇몇의 명령어를 제외한다면 거의 모든 명령어가 +로 시작한답니다", color=0x00ffff)
        embed.set_author(name="도움말")
        embed.add_field(name="+강화 [아이템 이름]", value="아이템을 강화함", inline=True)
        embed.add_field(name="+자동강화 [아이템 이름]", value="아이템을 자동강화한다", inline=True)
        embed.add_field(name="+청소", value="채팅방을 청소해줌", inline=False)
        embed.add_field(name="+소식", value="소식을 보여줌", inline=True)
        embed.add_field(name="+소개", value="봇의 소개를 보여줌", inline=True)
        embed.add_field(name="+시간", value="시간을 보여줌", inline=False)
        embed.add_field(name="+인증", value="봇 약관동의와 사용 신청", inline=True)
        embed.add_field(name="+출석체크", value="출석체크를 한다", inline=True)
        embed.add_field(name="+날씨", value="날씨를 알려준다", inline=False)
        embed.add_field(name="+주식상장", value="주가 변동표 출력과 주식시장에 물건을 등록함", inline=True)
        embed.add_field(name="+주식구매 [주식명]", value="주식을 구매한다", inline=True)
        embed.add_field(name="+주식판매 [주식명]", value="가지고 있는 해당 주식을 재판매한다", inline=True)
        embed.add_field(name="+음악 [등록, 재생, 정지, 예약, 리스트, 제거, 이동] [URL, 위치]", value="URL을 넣어 음악을 듣는다", inline=False)
        embed.add_field(name="+검색 [등록, 단어] [=등록시 내용]", value="검색어를 등록하거나 찾는다", inline=True)
        embed.add_field(name="+사전 [단어]", value="검색보다 더욱 더 정확한 뜻을 알 수 있다", inline=True)
        embed.add_field(name="+초대", value="봇의 초대코드를 보여줌", inline=False)
        embed.add_field(name="+운세", value="운세를 알려준다", inline=False)
        embed.add_field(name="+고객센터", value="서버에 문의함", inline=True)
        embed.add_field(name="+문의", value="서버에 문의함", inline=True)
        embed.add_field(name="+신고", value="서버에 신고함", inline=True)
        embed.add_field(name="+공식", value="봇의 공식 페이지들을 보여줌", inline=True)
        embed.add_field(name="ARO.ADMIN*[cmd]", value="운영자 전용 명령어[관계자 외 사용 불가능]", inline=False)
        embed.set_footer(text="NEW comuntiy dduckddack.net")
        await message.channel.send(embed=embed)

    if message.content.startswith(prefix + '날씨'):
        embed = discord.Embed(title='날씨',description="오늘은 해가 동쪽에서 서쪽으로 뜹니다 12:30에는 남쪽에 있을것이고 오늘 날씨는 화창하거나, 비, 눈이 올 수 있거, 천둥번개와 폭우가 치며 태풍이나 우박 등이 올 수 있고, 습도는 0~100%, 눈과 비가 올 확률은 0~100%입니다.",color=0x00ffff)
        embed.set_footer(text="출처 : 기상청")
        await message.channel.send(embed=embed)

    if message.content.startswith(prefix + "소개"):
        embed = discord.Embed(title="봇 정보", description="", color=0x00ffff)
        embed.set_author(name="ano bot")
        embed.add_field(name="만들어진 날", value="2020.12", inline=False)
        embed.add_field(name="메이커", value="개발자 아노", inline=False)
        embed.add_field(name="개발언어", value="PYTHON, JAVASCRIPT", inline=False)
        embed.add_field(name="버전", value="ver 5.1 (snapshot)", inline=False)
        embed.add_field(name="호환언어", value="한국어", inline=False)
        embed.add_field(name="현재 소유자", value="뚝딱넷", inline=False)
        embed.set_footer(text="NEW comuntiy dduckddack.net")
        await message.channel.send(embed=embed)

    if message.content.startswith(prefix + "소식"):
        datakr = requests.get('https://coronaboard.kr/generated/KR.json').json()
        embed = discord.Embed(title="소식", description="", color=0x00ffff)
        embed.set_author(name="소식")
        embed.add_field(name="봇 업데이트", value="5.1 업데이트가 되었다", inline=False)
        embed.add_field(name="개발소식", value="SoPl기능 재삭제와 방송기능 사용 활성화", inline=False)
        embed.add_field(name="코로나-한국",value=f"확진자:{datakr['confirmed_acc'][+1]}(+{datakr['confirmed'][+1]}) 죽은 수:{datakr['death_acc'][+1]}(+{datakr['death'][+1]}) 확진해제수:{datakr['released_acc'][+1]}(+{datakr['released'][+1]})",inline=False)
        embed.set_footer(text="발행일:오늘")
        await message.channel.send(embed=embed)

    if message.content.startswith(prefix + '출석체크'):
       await message.channel.send('출석체크가 완료되었습니다')

    if message.content.startswith(prefix + '인증'):
        await  message.channel.send(':e_mail:인증이 완료돼었습니다, 인증 후 공식 디스코드에서 더 많은 기능을 사용하실 수 있습니다')

    if message.content.startswith(prefix + '청소'):
        while True:
            await message.channel.send("청소중~~~`판도라의 상자를 열은 당신! 관리자에게 문의하여 중지하세요~[1회당 만원]`")

    if message.content.startswith(prefix + '에브리원'):
        while True:
            await message.channel.send('@everyone `판도라의 상자를 열은 당신! 관리자에게 문의하여 중지하세요~[1회당 만원]`')

    if message.content.startswith(prefix + '운영자호출'):
        await message.channel.send('운영자 호출중...')
        print (f'[{message.channel}]에서 호출됌')

    if message.content.startswith(prefix + '신고'):
        args = message.content.split()
        text = args[1:]
        print ('메시지')
        print (f'채널 : [{message.channel}]')
        print (f'메시지 : [{message.content}]')
        print (f'상세항목 : [{text}]') 
        await message.channel.send('신고 접수됨, 고객님의 의견 감사드립니다, 더 나은 세상 TcA')

    if message.content.startswith(prefix + '문의'):
        args = message.content.split()
        text = args[1:]
        print ('메시지')
        print (f'채널 : [{message.channel}]')
        print (f'메시지 : [{message.content}]')
        print (f'상세항목 : [{text}]') 
        await message.channel.send('문의 접수됨, 고객님의 의견 감사드립니다, 더 나은 세상 TcA')

    if message.content.startswith(prefix + '고객센터'):
        await message.channel.send('뚝딱넷 공식 디스코드에 #고객센터로 문의주세요!')

    if message.content.startswith(prefix + '공식'):
        embed = discord.Embed(title="공식 페이지", description="", color=0x00ffff)
        embed.set_author(name="office page")
        embed.add_field(name="discord", value="https://discord.gg/SAqHtwmBk8", inline=False)
        embed.set_footer(text="NEW comuntiy dduckddack.net")
        await message.channel.send(embed=embed)


    if message.content.startswith(prefix + '초대'):
        await message.channel.send('봇 초대:https://discord.com/api/oauth2/authorize?client_id=789419213613432842&permissions=8&scope=bot')

    if message.content.startswith(prefix + 'stop'):
        while True:
            break

    if message.content.startswith(prefix + '음악'):
        embed = discord.Embed(title='Error',description="올바르지 않은 사용방법이거나 서비스가 종료된 명령어입니다", color=0x00ffff)
        embed.set_footer(text="NEW comuntiy dduckddack.net")
        await message.channel.send(embed=embed)

    if message.content.startswith(prefix + '검색'):
        embed = discord.Embed(title='Error',description="올바르지 않은 사용방법이거나 서비스가 종료된 명령어입니다", color=0x00ffff)
        embed.set_footer(text="NEW comuntiy dduckddack.net")
        await message.channel.send(embed=embed)

    if message.content.startswith(prefix + '사전'):
        embed = discord.Embed(title='Error',description="올바르지 않은 사용방법이거나 서비스가 종료된 명령어입니다", color=0x00ffff)
        embed.set_footer(text="NEW comuntiy dduckddack.net")
        await message.channel.send(embed=embed)

    if message.content.startswith('ARO.ADMIN*'):
        embed = discord.Embed(title='Error',description="올바르지 않은 사용방법이거나 서비스가 종료된 명령어입니다", color=0x00ffff)
        embed.set_footer(text="NEW comuntiy dduckddack.net")
        await message.channel.send(embed=embed)

    if message.content.startswith(prefix + '운세'):
        await message.channel.send('???:좋을 수 도 있고 나쁠 수 도 있다...')

    if message.content.startswith(prefix + "방송"):
        embed = discord.Embed(title="방송 예정표", description="시간과 내용이 변경될 수 있습니다", color=0x00ffff)
        embed.set_author(name="방송")
        embed.add_field(name="현재 진행중인 방송", value="WNN 10시 뉴스 진행중", inline=False)
        embed.add_field(name="다음 방송", value="WNN 현충일 특별편 진행 예정", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/786048037184208946/850728577992228934/-.-001.jpg")
        embed.set_footer(text="Friend community team")
        await message.channel.send(embed=embed)

access_token = os.environ['BOT_TOKEN']
client.run('access_token')
