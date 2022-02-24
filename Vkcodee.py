from colorama import Fore, Back
from time import sleep
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait
import os
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions
import time
from time import sleep
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
app = Client('dedinside-session', api_id=1016382, api_hash='c27834e5683d50a9bacf835a95ec4763')

app.start()

app.stop()
print('''
      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
      ┃       Made by Vkcodee               Созданно Vkcodee       ┃
      ┃  Telegram: @vkcodee    Телеграм-канал: @Vkcodee  ┃
      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


''')
print("После ввода задержки напишите в любой телеграм чат Люблю тебя  <скорость до 10> \n Например: Люблю 8")
print()
cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))
if cool == 0:
    print("Слишком быстро!")
    cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))
if cool > 10:
    print("Слишком медленно!")
    cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))
if cool < 5:
    print("Слишком быстро!")
    cool = int(input("Введите завис.число - от него будет зависеть скорость(Норма 8):  "))
    

@app.on_message(filters.command("Люблю", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = textded.split("\n")
    e = True
    etime = int(msg.text.split('.Люблю', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                msg.delete()
            except:
                pass
        else:
            try:
                msg.edit(f'💚{i} ❤️')
                sleep(time/cool)
                msg.edit(f'❤️ {i} 🧡')
                sleep(time/cool)
                msg.edit(f'💛 {i} 💛')
                sleep(time/cool)
                msg.edit(f'💚 {i} 🧡')
                sleep(time/cool)
                msg.edit(f'💜 {i} 💙')
                sleep(time/cool)
                msg.edit(f'💙 {i} 💜')
                sleep(time/cool)
                msg.edit(f'🖤 {i} 🖤')
                sleep(time/cool)
                msg.edit(f'♡ {i} ♡')
                sleep(time/1)
            except:
                pass
    msg.edit(f'<b> ❤️❤️❤️ </b>')

textded = '''
<b> Я. </b>
<b> Я.. </b>
<b> Я... </b>
<b> Очень. </b>
<b> Очень.. </b>
<b> Очень... </b>
<b> Сильно. </b>
<b> Сильно.. </b>
<b> Сильно... </b>
<b> Люблю. </b>
<b> Люблю.. </b>
<b> Люблю... </b>
<b> Т </b>
<b> Т♡ </b>
<b> Т♡Е </b>
<b> Т♡Е♡ </b>
<b> Т♡Е♡Б </b>
<b> Т♡Е♡Б♡ </b>
<b> Т♡Е♡Б♡Я </b>
'''



app.run()


