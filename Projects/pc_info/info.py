# за работу с ОС и локаль­ными ресур­сами отве­чают эти четыре модуля:
import getpass # нужен для опре­деле­ния информа­ции о поль­зовате­ле;
import os # исполь­зуем для вза­имо­дей­ствия с фун­кци­ями ОС, вро­де вызова внеш­них исполня­емых фай­лов;
import psutil # работа­ет с некото­рыми низ­коуров­невыми сис­темны­ми фун­кци­ями;
# python -m pip install --upgrade pip # to upgrade module
# sudo pip install --upgrade psutil # install psutil
import platform # пре­дос­тавит информа­цию об ОС.

# Эти­ми модуля­ми реали­зова­ны сетевые вза­имо­дей­ствия
import socket # для работы с сокета­ми и получе­ния IP-адре­сов;
from uuid import getnode as get_mac # получа­ет MAC-адрес машины;
from speedtest import Speedtest #замеря­ет харак­терис­тики интернет‑соеди­нения;
# https://pypi.org/project/speedtest-cli/
# import telebot # сде­лает всю рутину по работе с Telegram-ботом.

# Слу­жеб­ные при­моч­ки, которые труд­но отнести к катего­риям выше:
import pyautogui # ""быс­тро и без боли"" работа­ет с GUI;
# < https://pyautogui.readthedocs.io/en/latest/install.html
from PIL import Image # для сня­тия скрин­шота.
# < Documentation
# https://pillow.readthedocs.io/en/stable/installation.html
from datetime import datetime # поз­волит опре­делить вре­мя работы прог­раммы;



# Get needed variables with information
name = getpass.getuser() # User name
# ip = socket.gethostbyname(socket.getfqdn()) # IP address of the system
ip = socket.gethostbyname(socket.gethostname()) # IP address of the system
mac = get_mac() # MAC address
ost = platform.uname() # Operating System (OS) name


# Do speed test of the network
inet = Speedtest()
# Входящая скорость
download = float(str(inet.download())[0:2] + "." + str(round(inet.download(), 2))[1]) * 0.125
# Исходящая скорость
uploads = float(str(inet.upload())[0:2] + "." + str(round(inet.download(), 2))[1]) * 0.125
# Ско­рость замеря­ется биб­лиоте­кой сер­виса Speedtest.net и, соот­ветс­твен­но,
# выда­ет резуль­тат в мегаби­тах, а не мегабай­тах. Что­бы это испра­вить,
# раз­делим чис­ленный резуль­тат на 8 или умно­жим на 0,125 — это одно и то же.
# Манипу­ляцию про­делы­ваем дваж­ды — для вхо­дящей и исхо­дящей ско­рос­ти.


# Часовой пояс и время import psutil
zone = psutil.boot_time() # Узнаёт время заданное на компьюторе
time = datetime.fromtimestamp(zone) # Переводит данные в читаемый вид

print(f"User name = {name}.")
print(f"IP address is {ip}.")
print(f"MAC address is {mac}.")
print(f"OS is {ost}.")
print(f"Download speed is {download} Mbit/s.")
print(f"Upload speed is {uploads} Mbit/s.")
print(f"Computer's time is {time}.")
