import telebot
from telebot import types

bot = telebot.TeleBot('5780337764:AAFgXajoCzxXVtBqvBlCPz8HeQIz23hcVDM')

@bot.message_handler(commands=['start'])
def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Наши ресурсы')
        btn2 = types.KeyboardButton('Перейти к заданиям')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Перейти к заданиям':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        back = types.KeyboardButton('Вернуться назад')
        btn1 = types.KeyboardButton('Задание №1')
        btn2 = types.KeyboardButton('Задание №2')
        btn3 = types.KeyboardButton('Задание №3')
        btn4 = types.KeyboardButton('Задание №4')
        markup.add(back, btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, 'Выберите задание:', reply_markup=markup) #ответ бота

    elif message.text == 'Наши ресурсы':
        markup = types.InlineKeyboardMarkup()
        url_button1 = types.InlineKeyboardButton(text="Сайт школы", url="https://sch2087uv.mskobr.ru/")
        url_button2 = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/sch2087")
        url_button3 = types.InlineKeyboardButton(text="Ученический кабинет", url="https://sites.google.com/mko2087.org/students")
        markup.add(url_button1, url_button2, url_button3)
        bot.send_message(message.chat.id, 'Наши ресурсы:', reply_markup=markup)

    elif message.text == 'Тест картинки':
        photo=open('logo1.png', 'rb')
        bot.send_photo(message.chat.id, photo)


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
