import telebot
import requests,time,os,sys
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

api = '1615187313:AAG2OQLTVdHZXkWiDcJI3rpS1e2e-Kpio5Q'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['2'])
def main(message):
	for u in range(0,99999999999999999999999999999999999999999999999999999999999999):
		url_json = url.json()
		pro = int(url_json['items'][0]['period'])+int(1)
		waktuku = int(url_json['items'][0]['endTime'])-int(url_json['items'][0]['beginTime'])-int(3)
		pro1 = int(url_json['items'][0]['period'])
		pertama = int(url_json['items'][0]['number']) + int(url_json['items'][2]['number'])
		kedua = int(url_json['items'][2]['number']) + int(url_json['items'][3]['number'])
		total1 = pertama + kedua
		ketiga = int(url_json['items'][7]['number']) + int(url_json['items'][9]['number'])
		total2 = total1 - ketiga
		x = int(url_json['items'][1]['period'][11]) + int(url_json['items'][0]['number'])
		y = int(url_json['items'][2]['period'][11]) + int(url_json['items'][1]['number'])
		empat = x - y
		# hasil = total2 + empat
		hasil = int(url_json['items'][0]['number']) - int(url_json['items'][7]['number'])
		if hasil%2 == 0 :
			bot.send_message(message.chat.id,"CEPAT PLUSS++\n"+str(pro)+"\U0001f34e\U0001f34e")
			# str(hasil))
		else:
			bot.send_message(message.chat.id,"CEPAT PLUSS++\n"+str(pro)+"\U0001f34f\U0001f34f")
			# str(hasil))

		for remaining in range(waktuku, 0, -1):
		    #sys.stdout.write("\r")
		    #sys.stdout.write("Time = {:2d}".format(remaining))
		    #sys.stdout.flush()
		    time.sleep(1)

		url = requests.get('https://lotre.io/api/main/game/rounds?page=1&count=90&type=3')
		url_json = url.json()
		if hasil%2 == 0 and int(url_json['items'][0]['number'])%2 == 0:
			bot.send_message(message.chat.id,str(pro)+"\U0001f34e\U0001f34e"+" WIN")
			main(message)
		if hasil%2 == 0 and int(url_json['items'][0]['number'])%2 == 1:
			bot.send_message(message.chat.id,str(pro)+"\U0001f34f\U0001f34f"+" LOSE")
			main(message)
		if hasil%2 == 1 and int(url_json['items'][0]['number'])%2 == 1:
			bot.send_message(message.chat.id,str(pro)+"\U0001f34f\U0001f34f"+" WIN")
			main(message)
		if hasil%2 == 1 and int(url_json['items'][0]['number'])%2 == 0:
			bot.send_message(message.chat.id,str(pro)+"\U0001f34e\U0001f34e"+" LOSE")
			main(message)

print('Bot Running!!')
bot.polling()
