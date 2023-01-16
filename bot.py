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
        btn2 = types.KeyboardButton('📘 Вариант №2 (ПУСТО)')
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
        bot.send_message(message.chat.id, 'Напишите наибольшее целое число x, для которого истинно высказывание:' + '\n' + '\n' + '(X > 5) И НЕ (X > 15).')
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
    elif message.text == '⏩ Следующее задание. В1-5':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-6')
        markup.add(back, btn1, btn2)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=ybwyb-CdNTg")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №5.',  reply_markup=markup)
        bot.send_message(message.chat.id, 'У исполнителя Делитель две команды, которым присвоены номера:' + '\n' + '\n' + '1. раздели на 2' + '\n' + '2.  вычти 1' + '\n' + '\n' + 'Первая из них уменьшает число на экране в 2 раза, вторая уменьшает его на 1. Исполнитель работает только с натуральными числами. Составьте алгоритм получения из чиcла 65 числа 4, содержащий не более 5 команд. В ответе запишите только номера команд.' + '\n' + '\n' + 'Например, 12112 – это алгоритм:' + '\n' + 'раздели на 2' + '\n' + 'вычти 1' + '\n' + 'раздели на 2'  + '\n' + 'раздели на 2'  + '\n' + 'вычти 1,'  + '\n' + 'который преобразует число 42 в число 4.' + '\n' + '\n' + 'Если таких алгоритмов более одного, то запишите любой из них.') 
        bot.send_message(message.chat.id,  f'Ответ: ||21111||', parse_mode='MarkdownV2',  reply_markup=markup2)
        
    # 1 ВАРИАНТ. ЗАДАНИЕ №6
    elif message.text == '⏩ Следующее задание. В1-6':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-7')
        markup.add(back, btn1, btn2)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=R2upK0ujKaQ")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №6.',  reply_markup=markup)
        bot.send_message(message.chat.id, 'Ниже приведена программа, записанная на пяти языках программирования.')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B1-6.png?raw=true')
        bot.send_message(message.chat.id, 'Было проведено 9 запусков программы, при которых в качестве значений переменных s и t вводились следующие пары чисел:' + '\n' + '\n' + '(6, 8); (3, 5); (–7, 2); (7, 7); (9, 8); (–1, 3); (–4, 5); (6, 9); (2, –1).'  + '\n' + '\n' + 'Сколько было запусков, при которых программа напечатала «YES»?')
        bot.send_message(message.chat.id,  f'Ответ: ||4||', parse_mode='MarkdownV2',  reply_markup=markup2) 
        
    # 1 ВАРИАНТ. ЗАДАНИЕ №7
    elif message.text == '⏩ Следующее задание. В1-7':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-8')
        markup.add(back, btn1, btn2)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=1qHXzmYnO7A")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №7.',  reply_markup=markup)
        bot.send_message(message.chat.id, 'Файл rose.gif был выложен в Интернете по адресу http://color.net/red/rose.gif. Потом его переместили в корневой каталог на сайте box.net, доступ к которому осуществляется по протоколу ftp. Имя файла не изменилось.' + '\n' + '\n' + 'Фрагменты нового и старого адресов файла закодированы цифрами от 1 до 9. Запишите последовательность этих цифр, кодирующую адрес файла в сети Интернет после перемещения.'  + '\n' + '\n' + '1) http:/'  + '\n' + '2) box'  + '\n' + '3) red'  + '\n' + '4) rose'  + '\n' + '5) .net'  + '\n' + '6) ftp:/'  + '\n' + '7) /'  + '\n' + '8) .gif'  + '\n' + '9) color')
        bot.send_message(message.chat.id,  f'Ответ: ||6725748||', parse_mode='MarkdownV2',  reply_markup=markup2) 

    # 1 ВАРИАНТ. ЗАДАНИЕ №8
    elif message.text == '⏩ Следующее задание. В1-8':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-9')
        markup.add(back, btn1, btn2)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=xxxI27oFs1E")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №8.',  reply_markup=markup)
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B1-8.png?raw=true')
        bot.send_message(message.chat.id,  f'Ответ: ||8770||', parse_mode='MarkdownV2',  reply_markup=markup2)

    # 1 ВАРИАНТ. ЗАДАНИЕ №9
    elif message.text == '⏩ Следующее задание. В1-9':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-10')
        markup.add(back, btn1, btn2)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=Xrjl7lv3sVM")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №9.',  reply_markup=markup)
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B1-9.png?raw=true')
        bot.send_message(message.chat.id,  f'Ответ: ||16||', parse_mode='MarkdownV2',  reply_markup=markup2)
 
    # 1 ВАРИАНТ. ЗАДАНИЕ №10
    elif message.text == '⏩ Следующее задание. В1-10':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-11')
        markup.add(back, btn1, btn2)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=HNXq5tJS8Fg")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №10.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'Среди приведённых ниже трёх чисел, записанных в десятичной системе счисления, найдите число, сумма цифр которого в восьмеричной записи наименьшая. В ответе запишите сумму цифр в восьмеричной записи этого числа.')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B1-10.png?raw=true')
        bot.send_message(message.chat.id,  f'Ответ: ||7||', parse_mode='MarkdownV2',  reply_markup=markup2) 
 
    # 1 ВАРИАНТ. ЗАДАНИЕ №11
    elif message.text == '⏩ Следующее задание. В1-11':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-12')
        markup.add(back, btn1, btn2)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="🗂️ Архив", url="https://drive.google.com/file/d/1J4iqJ2PLcNk4baYttwxLjtr9rowzIbxe/view?usp=share_link")
        url_button2 = types.InlineKeyboardButton(text="☁️ Облако", url="https://drive.google.com/drive/folders/1g3fTxVBxqUNJA4sXlwInyCsGoK1q4krf?usp=sharing")
        url_button3 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=7HfOEFw2K8g")
        markup2.add(url_button1,url_button2,url_button3)
        bot.send_message(message.chat.id, 'Задание №11.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'В одном из произведений Н.В.Гоголя, текст которого приведён в подкаталоге "Гоголь" каталога "Проза", присутствует персонаж Остап. С помощью поисковых средвств операционной системы и текстового редактора выясните имя брата этого персонажа.')
        bot.send_message(message.chat.id,  f'Ответ: ||Андрий||', parse_mode='MarkdownV2',  reply_markup=markup2) 
 
    # 1 ВАРИАНТ. ЗАДАНИЕ №12
    elif message.text == '⏩ Следующее задание. В1-12':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-13')
        markup.add(back, btn1, btn2)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="🗂️ Архив", url="https://drive.google.com/file/d/1pPIAZlVNlWnJh63jxOWIKdi5vTRkqLHq/view?usp=sharing")
        url_button2 = types.InlineKeyboardButton(text="☁️ Облако", url="https://drive.google.com/drive/folders/1vHNtO1wMOyNsyzL_HWS7yL4B7JpFfkFU?usp=share_link")
        url_button3 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=0DZw0af1cNE")
        markup2.add(url_button1,url_button2,url_button3)
        bot.send_message(message.chat.id, 'Задание №12.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'Сколько файлов с расширением .rtf содержится в подкаталогах каталога Task12? В ответе укажите только число.')
        bot.send_message(message.chat.id,  f'Ответ: ||10||', parse_mode='MarkdownV2',  reply_markup=markup2) 
 
    # 1 ВАРИАНТ. ЗАДАНИЕ №13
    elif message.text == '⏩ Следующее задание. В1-13':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-14')
        markup.add(back, btn1, btn2)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=z2vrViRw0iY")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №13.',  reply_markup=markup) 
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B1-13.png?raw=true',  reply_markup=markup2)
 
    # 1 ВАРИАНТ. ЗАДАНИЕ №14
    elif message.text == '⏩ Следующее задание. В1-14':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-15')
        markup.add(back, btn1, btn2)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="🗂️ Архив", url="https://drive.google.com/file/d/1D8YCYdhKQNd1UEZMBBMwA-V_6YM85R8T/view?usp=share_link")
        url_button2 = types.InlineKeyboardButton(text="☁️ Облако", url="https://docs.google.com/spreadsheets/d/19TivcKih_GsWB0O_OCL0mViepi-ig6md/edit?usp=share_link&ouid=104878964026869489773&rtpof=true&sd=true")
        url_button3 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=Oh3ijrnQ850")
        markup2.add(url_button1,url_button2,url_button3)
        bot.send_message(message.chat.id, 'Задание №14.',  reply_markup=markup) 
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B1-14.png?raw=true')
        bot.send_message(message.chat.id,  f'Ответ: ||1) 21 ; 2) 52||', parse_mode='MarkdownV2',  reply_markup=markup2) 
 
    # 1 ВАРИАНТ. ЗАДАНИЕ №15
    elif message.text == '⏩ Следующее задание. В1-15':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        markup.add(back, btn1)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=1y8sE9xGUNE")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №15.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'На бесконечном поле имеются две вертикальные стены и одна горизонтальная, соединяющая нижний конец левой и верхний конец правой вертикальных стен. Длины стен неизвестны. Робот находится в клетке, расположенной слева от нижнего края правой вертикальной стены, рядом со стеной. На рисунке указан один из возможных способов расположения стен и Робота (Робот обозначен буквой «Р»).')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B1-15-1.png?raw=true')
        bot.send_message(message.chat.id, 'Напишите для Робота алгоритм, закрашивающий все клетки, примыкающие к вертикальным стенам справа. Робот должен закрасить только клетки, удовлетворяющие данному условию. Например, для приведённого выше рисунка Робот должен закрасить следующие клетки (см. рис.).')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B1-15-2.png?raw=true')
        bot.send_message(message.chat.id, 'Конечное расположение Робота может быть произвольным. Алгоритм должен решать задачу для произвольного размера поля и любого допустимого расположения стен внутри прямоугольного поля. При исполнении алгоритма Робот не должен разрушиться, выполнение алгоритма должно завершиться. Алгоритм может быть выполнен в среде формального исполнителя или  записан в текстовом редакторе. Сохраните алгоритм в формате программы Кумир или в текстовом файле. Название файла и каталог для сохранения Вам сообщат организаторы экзамена.')
        bot.send_message(message.chat.id,  f'Ответ: ||1) 21 <br> ; 2) 52||', parse_mode='MarkdownV2',  reply_markup=markup2) 

bot.polling(none_stop=True, interval=0)
