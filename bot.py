import telebot
from telebot import types

bot = telebot.TeleBot('5780337764:AAFgXajoCzxXVtBqvBlCPz8HeQIz23hcVDM')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник! 222", reply_markup=markup)


@bot.message_handler(commands=['start2'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Сайт школы')
        btn2 = types.KeyboardButton('Вконтакте школы')
        btn3 = types.KeyboardButton('Ученический кабинет')
        btn4 = types.KeyboardButton('Тест картинки')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота

    elif message.text == 'Сайт школы':
        bot.send_message(message.from_user.id, 'Перейдите по ' + '[ссылке](https://sch2087uv.mskobr.ru/)', parse_mode='Markdown')

    elif message.text == 'Вконтакте школы':
        bot.send_message(message.from_user.id, 'Перейдите по ' + '[ссылке](https://vk.com/sch2087)', parse_mode='Markdown')

    elif message.text == 'Ученический кабинет':
        bot.send_message(message.from_user.id, 'Перейдите по ' + '[ссылке](https://sites.google.com/mko2087.org/students/daijest)', parse_mode='Markdown')

    elif message.text == 'Тест картинки':
        photo=open('pics\logo1.png', 'rb')
        bot.send_photo(message.chat.id, photo)


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
