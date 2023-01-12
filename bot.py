import telebot
from telebot import types

bot = telebot.TeleBot('5780337764:AAFgXajoCzxXVtBqvBlCPz8HeQIz23hcVDM')

@bot.message_handler(commands=['start'])
def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('🌐 Наши ресурсы')
        btn2 = types.KeyboardButton('📝 Перейти к заданиям')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, '✅ Выберите действие:', reply_markup=markup) 

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    # ГЛАВНОЕ МЕНЮ     
    if message.text == '❇️ Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('🌐 Наши ресурсы')
        btn2 = types.KeyboardButton('📝 Перейти к заданиям')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, '✅ Выберите действие:', reply_markup=markup) 
   
    # НАШИ РЕСУРСЫ        
    elif message.text == '🌐 Наши ресурсы':
        markup = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="Сайт школы", url="https://sch2087uv.mskobr.ru/")
        url_button2 = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/sch2087")
        url_button3 = types.InlineKeyboardButton(text="Ученический кабинет", url="https://sites.google.com/mko2087.org/students")
        markup.add(url_button1, url_button2, url_button3)
        bot.send_message(message.chat.id, '🌐 Наши ресурсы 🌐', reply_markup=markup)
        
    # ВЫБОР ВАРИАНТОВ  
    elif message.text == '📝 Перейти к заданиям':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📕 Вариант №1')
        btn2 = types.KeyboardButton('📘 Вариант №2')
        markup.add(back, btn1, btn2)
        bot.send_message(message.from_user.id, '📍 Выберите вариант:', reply_markup=markup) 
    
    # 1 ВАРИАНТ
    # 1 ВАРИАНТ. ЗАДАНИЕ №1
    elif message.text == '📕 Вариант №1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-2')
        markup.add(back, btn1, btn2)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=9H9xAK3Y25o")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №1.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'В одной из кодировок Unicode каждый символ кодируется 16 битами. Вова написал текст (в нём нет лишних пробелов):' + '\n' + '\n' + '«Чиж, грач, стриж, гагара, пингвин, ласточка, жаворонок, свиристель, буревестник, вертиголовка — птицы».' + '\n' + '\n' + 'Ученик вычеркнул из списка название одной птицы. Заодно он вычеркнул ставшие лишними запятые и пробелы — два пробела не должны идти подряд. При этом размер нового предложения в данной кодировке оказался на 12 байт меньше, чем размер исходного предложения. Напишите в ответе вычеркнутое название птицы.') 
        bot.send_message(message.chat.id,  f'Ответ: ||Грач||', parse_mode='MarkdownV2',  reply_markup=markup2) 

    # 1 ВАРИАНТ. ЗАДАНИЕ №2
    elif message.text == '⏩ Следующее задание. В1-2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-3')
        markup.add(back, btn1, btn2)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=CEtG5MUmvWM")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №2.',  reply_markup=markup)
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B1-2.png?raw=true')
        bot.send_message(message.chat.id,  f'Ответ: ||5||', parse_mode='MarkdownV2',  reply_markup=markup2)
 
    # 1 ВАРИАНТ. ЗАДАНИЕ №3
    elif message.text == '⏩ Следующее задание. В1-3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-4')
        markup.add(back, btn1, btn2)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://youtu.be/Ekrt54b_8as")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №3.',  reply_markup=markup) 
        bot.send_photo(message.chat.id, 'Напишите наибольшее целое число x, для которого истинно высказывание:' + '\n' + '\n' + '(X > 5) И НЕ (X > 15).')
        bot.send_message(message.chat.id,  f'Ответ: ||15||', parse_mode='MarkdownV2',  reply_markup=markup2) 

    # 1 ВАРИАНТ. ЗАДАНИЕ №4
    elif message.text == '⏩ Следующее задание. В1-4':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-5')
        markup.add(back, btn1, btn2)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=Ekrt54b_8as")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №4.',  reply_markup=markup)
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B1-4.png?raw=true')
        bot.send_message(message.chat.id,  f'Ответ: ||9||', parse_mode='MarkdownV2',  reply_markup=markup2) 
        
    # 1 ВАРИАНТ. ЗАДАНИЕ №5
    elif message.text == '⏩ Следующее задание. В1-6':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-6')
        markup.add(back, btn1, btn2)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=ybwyb-CdNTg")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №5.',  reply_markup=markup)
        bot.send_message(message.chat.id, 'У исполнителя Делитель две команды, которым присвоены номера:' + '\n' + '\n' + '1. раздели на 2' + '\n' + '2.  вычти 1' + '\n' + 'Первая из них уменьшает число на экране в 2 раза, вторая уменьшает его на 1. Исполнитель работает только с натуральными числами. Составьте алгоритм получения из чиcла 65 числа 4, содержащий не более 5 команд. В ответе запишите только номера команд.' + '\n' + '\n' + 'Например, 12112 – это алгоритм:' + '\n' + 'раздели на 2' + '\n' + 'вычти 1' + '\n' + 'раздели на 2'  + '\n' + 'раздели на 2'  + '\n' + 'вычти 1,'  + '\n' + 'который преобразует число 42 в число 4.' + '\n' + '\n' + 'Если таких алгоритмов более одного, то запишите любой из них./') 
        bot.send_message(message.chat.id,  f'Ответ: ||21111||', parse_mode='MarkdownV2',  reply_markup=markup2)

bot.polling(none_stop=True, interval=0)
