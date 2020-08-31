# Голосовой ассистент Марго, версия 1.1 BETA

import speech_recognition as sr
import pyttsx3
import os
import sys
import webbrowser
import datetime as dt 
import time
import random as rd 

def listen():
	r = sr.Recognizer() 
	mic = sr.Microphone(device_index=1)
	engine = pyttsx3.init()
	with mic as source:
		engine.say('Я вас слушаю')
		engine.runAndWait()
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration=1) 
		audio = r.listen(source) 
	try:
		voice = r.recognize_google(audio, language="ru-RU").lower() 
		print('- ' + voice) 
	except:
		engine.say('Ваш голос не распознан')
		engine.runAndWait()
		voice = listen() 
	return voice

def commands(voice):
	engine = pyttsx3.init()
	global startTime
	if 'привет' in voice: 
		time_now = dt.datetime.now()
		if 6 <= time_now.hour < 12:
			engine.say('Доброе утро')
		elif 12 <= time_now.hour < 18:
			engine.say('Добрый день')
		elif 18 <= time_now.hour < 23:
			engine.say('Добрый вечер')
		else:
			engine.say('Доброй ночи')
	elif voice == 'открой вконтакте':
		engine.say('Открываю ВК')
		url = 'https://vk.com/feed'
		webbrowser.open(url)
	elif 'открой youtube' in voice:
		engine.say('Открываю Ютуб')
		url = 'https://www.youtube.com/'
		webbrowser.open(url)
	elif 'открой habr' in voice:
		engine.say('Открываю Хабр')
		url = 'https://habr.com/ru/'
		webbrowser.open(url)
	elif 'сколько время' in voice:
		period = dt.timedelta(hours=3)
		now_time = dt.datetime.utcnow()
		moment = period + now_time
		engine.say('Сейчас ' + moment.strftime('%H:%M') + ' по Москве')
	elif 'какая сегодня дата' in voice:
		now_date = dt.datetime.utcnow()
		engine.say('Сегодняшняя дата: ' + now_date.strftime('%d:%m:%Y'))
	elif 'включи секундомер' in voice:
		engine.say('Секундомер запущен')
		startTime = time.time()
	elif 'выключить секундомер' in voice:
		if startTime != 0:
			Time = time.time() - startTime
			engine.say('Секундомер отключен')
			engine.say('Прошло: ' + str(round(Time // 3600)) + ' часов,' + str(round(Time // 60)) + 'минут, ' + str(round(Time % 60)) + ' секунд.')
			startTime = 0
		else:
			engine.say('Секундомер не запущен')
	elif 'орёл или решка' in voice:
		coin_list = ['Орёл', 'Решка']
		coin_up = rd.choice(coin_list)
		engine.say(str(coin_up))
	elif 'пока' in voice:
		engine.say('Я отключаюсь')
		engine.runAndWait()
		sys.exit()
	else:
		engine.say('Неизвестный запрос')
	engine.runAndWait()

while True:
	commands(listen())