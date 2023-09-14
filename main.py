import os
import random
import schedule
import telebot
from telebot import TeleBot
from telebot import types
import time


lang: TeleBot = telebot.TeleBot('6660554674:AAHp611_XyglwKs9zb9HV_o_KGFKJeT8JbI')


@lang.message_handler(commands=['menu'], content_types=['text', 'photo', 'audio', 'media', 'video'])
def start(message):
    pic = open('mainphoto/' + '20200620103430-001-Panorama-1024x720.jpg', 'rb')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn2 = types.KeyboardButton("Получить карту!")
    markup.add(btn2)
    lang.send_photo(message.from_user.id, pic, caption='Добро пожаловать в <b>Битбокс хаус</b>! Выбирай, что тебе нужно посмотреть!', parse_mode='html', reply_markup=markup)


@lang.message_handler(commands=['start'], content_types=['text', 'photo', 'audio', 'media', 'video'])
def start(message):
    pic1 = open('mainphoto/' + 'maxresdefault.jpg', 'rb')
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn4 = types.KeyboardButton("Главное меню")
    markup3.add(btn4)
    lang.send_photo(message.from_user.id, pic1, caption='Привет, пользователь! Добро пожаловать в бота BeatboxCollection! Начинаем?', parse_mode='html', reply_markup=markup3)



@lang.message_handler(content_types=['text', 'photo', 'audio', 'media', 'video'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn2 = types.KeyboardButton("Получить карту!")
    btn1 = types.KeyboardButton("Назад")
    markup.add(btn1, btn2)
    pic = open('mainphoto/' + '20200620103430-001-Panorama-1024x720.jpg', 'rb')
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn2 = types.KeyboardButton("Получить еще!")
    btn1 = types.KeyboardButton("Назад")
    markup2.add(btn1, btn2)
    if message.text == "Получить карту!":
        photo = open('photos/' + random.choice(os.listdir('photos')), 'rb')
        lang.send_photo(message.from_user.id, photo, caption='Держи свою карту, бро!', reply_markup=markup2)
    elif message.text == "Главное меню":
        lang.send_photo(message.from_user.id, pic,
                            caption='Добро пожаловать в <b>Битбокс хаус</b>! Выбирай, что тебе нужно посмотреть!',
                            parse_mode='html', reply_markup=markup)
    elif message.text == "Получить еще!":
        schedule.every(10).minutes.do(lang.send_photo(message.from_user.id, photo, caption='Держи свою карту, бро!', reply_markup=markup2))
        while True:
            schedule.run_pending()
            time.sleep(1)
            photo = open('photos/' + random.choice(os.listdir('photos')), 'rb')
            lang.send_photo(message.from_user.id, photo, caption='Держи свою карту, бро!', reply_markup=markup2)
    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton("Получить карту!")
        markup.add(btn2)
        lang.send_photo(message.from_user.id, pic,
                        caption='Добро пожаловать в <b>Битбокс хаус</b>! Выбирай, что тебе нужно посмотреть!',
                        parse_mode='html', reply_markup=markup)
    else:
        lang.send_message(message.chat.id,'Я не знаю такого, давай попробуем еще разок')


lang.polling(none_stop=True, interval=0)
