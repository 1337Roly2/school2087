import telebot
from telebot import types

bot = telebot.TeleBot('5780337764:AAFgXajoCzxXVtBqvBlCPz8HeQIz23hcVDM')

@bot.message_handler(commands=['start'])
def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('🌐 Наши ресурсы')
        btn2 = types.KeyboardButton('📝 Перейти к заданиям')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, '✅ Выберите действие:', reply_markup=markup) #ответ бота

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '📝 Перейти к заданиям':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📕 Вариант №1')
        btn2 = types.KeyboardButton('📘 Вариант №2')
        markup.add(back, btn1, btn2)
        bot.send_message(message.from_user.id, '📍 Выберите вариант:', reply_markup=markup) #ответ бота
    
    # 1 ВАРИАНТ
    # 1 задания
    elif message.text == '📕 Вариант №1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-2')
        markup.add(back, btn1, btn2)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео разбор", url="https://www.youtube.com/watch?v=9H9xAK3Y25o")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №1.' + '\n' + '\n' + 'В одной из кодировок Unicode каждый символ кодируется 16 битами. Вова написал текст (в нём нет лишних пробелов):' + '\n' + '\n' + '«Чиж, грач, стриж, гагара, пингвин, ласточка, жаворонок, свиристель, буревестник, вертиголовка — птицы».' + '\n' + '\n' + 'Ученик вычеркнул из списка название одной птицы. Заодно он вычеркнул ставшие лишними запятые и пробелы — два пробела не должны идти подряд. При этом размер нового предложения в данной кодировке оказался на 12 байт меньше, чем размер исходного предложения. Напишите в ответе вычеркнутое название птицы.' ,  reply_markup=markup) #ответ бота
        bot.send_message(message.chat.id,  f'Ответ: ||Грач||', parse_mode='MarkdownV2',  reply_markup=markup2) #ответ бота
        
    elif message.text == '⏩ Следующее задание. В1-2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-3')
        markup.add(back, btn1)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео разбор", url="hhttps://www.youtube.com/watch?v=CEtG5MUmvWM")
        markup2.add(url_button1)
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B1-2.png?raw=true')
        bot.send_message(message.chat.id,  f'Ответ: ||5||', parse_mode='MarkdownV2',  reply_markup=markup2) #ответ бота
    
    elif message.text == '⏩ Следующее задание. В1-3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        markup.add(back, btn1)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео разбор", url="https://youtu.be/Qc_bor8hnCQ")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №1.' + '\n' + '\n' + 'Сколько будет 2+2?',  reply_markup=markup) #ответ бота
        bot.send_message(message.chat.id,  f'Ответ: ||4||', parse_mode='MarkdownV2',  reply_markup=markup2) #ответ бота
    
    elif message.text == 'Задание №3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        markup.add(back, btn1)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео разбор", url="https://youtu.be/Qc_bor8hnCQ")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №1.' + '\n' + '\n' + 'Сколько будет 3+3?',  reply_markup=markup) #ответ бота
        bot.send_message(message.chat.id,  f'Ответ: ||26||', parse_mode='MarkdownV2',  reply_markup=markup2) #ответ бота
    
    
    elif message.text == 'Задание №4':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        markup.add(back, btn1)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео разбор", url="https://youtu.be/Qc_bor8hnCQ")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №1.' + '\n' + '\n' + 'Сколько будет 4+4?',  reply_markup=markup) #ответ бота
        bot.send_message(message.chat.id,  f'Ответ: ||8||', parse_mode='MarkdownV2',  reply_markup=markup2) #ответ бота
        
    elif message.text == '❇️ Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('🌐 Наши ресурсы')
        btn2 = types.KeyboardButton('📝 Перейти к заданиям')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, '✅ Выберите действие:', reply_markup=markup) #ответ бота
        
    elif message.text == '🌐 Наши ресурсы':
        markup = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="Сайт школы", url="https://sch2087uv.mskobr.ru/")
        url_button2 = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/sch2087")
        url_button3 = types.InlineKeyboardButton(text="Ученический кабинет", url="https://sites.google.com/mko2087.org/students")
        markup.add(url_button1, url_button2, url_button3)
        bot.send_message(message.chat.id, '🌐 Наши ресурсы 🌐', reply_markup=markup)

    elif message.text == 'Тест картинки':
        #photo=open(url='https://github.com/1337Roly2/school2087/blob/main/pics/logo1.png', 'rb')
        #bot.send_photo(message.chat.id, photo)
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/logo1.png?raw=true')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
