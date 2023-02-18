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
        btn3 = types.KeyboardButton('📙 Вариант №3')
        markup.add(btn1, btn2, btn3)
        markup.row(back)
        bot.send_message(message.from_user.id, '📍 Выберите вариант:', reply_markup=markup) 
    
    # 1 ВАРИАНТ
    # 1 ВАРИАНТ. ЗАДАНИЕ №1
    elif message.text == '📕 Вариант №1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-2')
        markup.add(btn1, btn2)
        markup.row(back)
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
        markup.add(btn1, btn2)
        markup.row(back)
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
        markup.add(btn1, btn2)
        markup.row(back)
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
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=8lv-35Y1yQY")
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
        markup.add(btn1, btn2)
        markup.row(back)
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
        markup.add(btn1, btn2)
        markup.row(back)
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
        markup.add(btn1, btn2)
        markup.row(back)
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
        markup.add(btn1, btn2)
        markup.row(back)
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
        markup.add(btn1, btn2)
        markup.row(back)
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
        markup.add(btn1, btn2)
        markup.row(back)
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
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="🗂️ Архив", url="https://drive.google.com/file/d/1J4iqJ2PLcNk4baYttwxLjtr9rowzIbxe/view?usp=share_link")
        url_button2 = types.InlineKeyboardButton(text="☁️ Облако", url="https://drive.google.com/drive/folders/1g3fTxVBxqUNJA4sXlwInyCsGoK1q4krf?usp=sharing")
        url_button3 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=7HfOEFw2K8g")
        markup3 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(url_button1,url_button2)
        markup3.add(url_button3)
        bot.send_message(message.chat.id, 'Задание №11.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'В одном из произведений Н.В.Гоголя, текст которого приведён в подкаталоге "Гоголь" каталога "Проза", присутствует персонаж Остап. С помощью поисковых средвств операционной системы и текстового редактора выясните имя брата этого персонажа.',  reply_markup=markup2)
        bot.send_message(message.chat.id,  f'Ответ: ||Андрий||', parse_mode='MarkdownV2',  reply_markup=markup3) 
 
    # 1 ВАРИАНТ. ЗАДАНИЕ №12
    elif message.text == '⏩ Следующее задание. В1-12':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-13')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="🗂️ Архив", url="https://drive.google.com/file/d/1pPIAZlVNlWnJh63jxOWIKdi5vTRkqLHq/view?usp=sharing")
        url_button2 = types.InlineKeyboardButton(text="☁️ Облако", url="https://drive.google.com/drive/folders/1vHNtO1wMOyNsyzL_HWS7yL4B7JpFfkFU?usp=share_link")
        url_button3 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=0DZw0af1cNE")
        markup3 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(url_button1,url_button2)
        markup3.add(url_button3)
        bot.send_message(message.chat.id, 'Задание №12.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'Сколько файлов с расширением .rtf содержится в подкаталогах каталога Task12? В ответе укажите только число.',  reply_markup=markup2)
        bot.send_message(message.chat.id,  f'Ответ: ||10||', parse_mode='MarkdownV2',  reply_markup=markup3) 
 
    # 1 ВАРИАНТ. ЗАДАНИЕ №13
    elif message.text == '⏩ Следующее задание. В1-13':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В1-14')
        markup.add(btn1, btn2)
        markup.row(back)
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
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="🗂️ Архив", url="https://drive.google.com/file/d/1D8YCYdhKQNd1UEZMBBMwA-V_6YM85R8T/view?usp=share_link")
        url_button2 = types.InlineKeyboardButton(text="☁️ Облако", url="https://docs.google.com/spreadsheets/d/19TivcKih_GsWB0O_OCL0mViepi-ig6md/edit?usp=share_link&ouid=104878964026869489773&rtpof=true&sd=true")
        url_button3 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=Oh3ijrnQ850")
        markup3 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(url_button1,url_button2)
        markup3.add(url_button3)
        bot.send_message(message.chat.id, 'Задание №14.',  reply_markup=markup) 
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B1-14.png?raw=true',  reply_markup=markup2)
        bot.send_message(message.chat.id,  f'Ответ: ||1\) 21 ; 2\) 52||', parse_mode='MarkdownV2',  reply_markup=markup3) 
 
    # 1 ВАРИАНТ. ЗАДАНИЕ №15
    elif message.text == '⏩ Следующее задание. В1-15':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        markup.add(btn1)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=1y8sE9xGUNE")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №15.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'На бесконечном поле имеются две вертикальные стены и одна горизонтальная, соединяющая нижний конец левой и верхний конец правой вертикальных стен. Длины стен неизвестны. Робот находится в клетке, расположенной слева от нижнего края правой вертикальной стены, рядом со стеной. На рисунке указан один из возможных способов расположения стен и Робота (Робот обозначен буквой «Р»).')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B1-15-1.png?raw=true')
        bot.send_message(message.chat.id, 'Напишите для Робота алгоритм, закрашивающий все клетки, примыкающие к вертикальным стенам справа. Робот должен закрасить только клетки, удовлетворяющие данному условию. Например, для приведённого выше рисунка Робот должен закрасить следующие клетки (см. рис.).')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B1-15-2.png?raw=true')
        bot.send_message(message.chat.id, 'Конечное расположение Робота может быть произвольным. Алгоритм должен решать задачу для произвольного размера поля и любого допустимого расположения стен внутри прямоугольного поля. При исполнении алгоритма Робот не должен разрушиться, выполнение алгоритма должно завершиться. Алгоритм может быть выполнен в среде формального исполнителя или  записан в текстовом редакторе. Сохраните алгоритм в формате программы Кумир или в текстовом файле. Название файла и каталог для сохранения Вам сообщат организаторы экзамена.')
        bot.send_message(message.chat.id,  f'Ответ: \n ||нц пока не справа свободно \n вниз \n кц \n \n вправо \n \n нц пока слева свободно \n вверх \n кц \n \n нц пока не слева свободно \n закрасить \n вверх \n кц \n \n нц пока слева свободно \n влево \n кц \n \n нц пока не слева свободно \n закрасить \n вверх \n кц||', parse_mode='MarkdownV2',  reply_markup=markup2) 
    # 2 ВАРИАНТ       
    # 2 ВАРИАНТ
    # 2 ВАРИАНТ
    # 2 ВАРИАНТ        
    # 2 ВАРИАНТ
    # 2 ВАРИАНТ. ЗАДАНИЕ №1
    elif message.text == '📘 Вариант №2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В2-2')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=9H9xAK3Y25o")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №1.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'В одной из кодировок Unicode каждый символ кодируется 16 битами. Вова написал текст (в нём нет лишних пробелов):' + '\n' + '\n' + '«Ёж, лев, слон, олень, тюлень, носорог, крокодил, аллигатор – дикие животные».' + '\n' + '\n' + 'Ученик вычеркнул из списка название одной птицы. Заодно он вычеркнул ставшие лишними запятые и пробелы — два пробела не должны идти подряд. При этом размер нового предложения в данной кодировке оказался на 12 байт меньше, чем размер исходного предложения. Напишите в ответе вычеркнутое название птицы.') 
        bot.send_message(message.chat.id,  f'Ответ: ||Слон||', parse_mode='MarkdownV2',  reply_markup=markup2)

    # 2 ВАРИАНТ. ЗАДАНИЕ №2
    elif message.text == '⏩ Следующее задание. В2-2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В2-3')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=CEtG5MUmvWM")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №2.',  reply_markup=markup)
        bot.send_message(message.chat.id, 'От разведчика было получено сообщение:'  + '\n' + '\n' + '100011010011100110' + '\n' + '\n' +  'В этом сообщении зашифрован пароль – последовательность русских букв. В пароле использовались только буквы А, Б, К, Л, О, С; каждая буква кодировалась двоичным словом по таблице, показанной на рисунке. Расшифруйте сообщение. Запишите в ответе пароль.')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B2-2.png?raw=true')
        bot.send_message(message.chat.id,  f'Ответ: ||баколос||', parse_mode='MarkdownV2',  reply_markup=markup2)
 
    # 2 ВАРИАНТ. ЗАДАНИЕ №3
    elif message.text == '⏩ Следующее задание. В2-3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В2-4')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://youtu.be/Ekrt54b_8as")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №3.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'Напишите наибольшее целое число x, для которого истинно высказывание:' + '\n' + '\n' + '(x > 35) И НЕ (x не делится на 7)')
        bot.send_message(message.chat.id,  f'Ответ: ||42||', parse_mode='MarkdownV2',  reply_markup=markup2) 

    # 2 ВАРИАНТ. ЗАДАНИЕ №4
    elif message.text == '⏩ Следующее задание. В2-4':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В2-5')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=8lv-35Y1yQY")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №4.',  reply_markup=markup)
        bot.send_message(message.chat.id, 'Между населёнными пунктами A, B, C, D, E построены дороги, протяжённость которых (в километрах) приведена в таблице. Определите длину кратчайшего пути между пунктами A и Е, проходящего через пункт D. Передвигаться можно только по дорогам, протяжённость которых указана в таблице.')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B2-4.png?raw=true')
        bot.send_message(message.chat.id,  f'Ответ: ||6||', parse_mode='MarkdownV2',  reply_markup=markup2) 
        
    # 2 ВАРИАНТ. ЗАДАНИЕ №5
    elif message.text == '⏩ Следующее задание. В2-5':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В2-6')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=ybwyb-CdNTg")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №5.',  reply_markup=markup)
        bot.send_message(message.chat.id, 'У исполнителя Альфа две команды, которым присвоены номера:' + '\n' + '\n' + '1. прибавь 1' + '\n' + ' 2. умножь на b' + '\n' + '\n' + '(b - неизвестное натуральное число; b ≥ 2) Выполняя первую из них, Альфа увеличивает число на экране на 1, а выполняя вторую, умножает это число на b. Известно, что программа 11211 переводит число 12 в число 114. Определите значение b.') 
        bot.send_message(message.chat.id,  f'Ответ: ||8||', parse_mode='MarkdownV2',  reply_markup=markup2)
        
    # 2 ВАРИАНТ. ЗАДАНИЕ №6
    elif message.text == '⏩ Следующее задание. В2-6':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В2-7')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=R2upK0ujKaQ")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №6.',  reply_markup=markup)
        bot.send_message(message.chat.id, 'Дана программа:')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B2-6.png?raw=true')
        bot.send_message(message.chat.id, 'Было проведено 9 запусков программы, при которых в качестве значений переменных s и t вводились следующие пары чисел:' + '\n' + '\n' + '(1, 2); (11, 2); (1, 12); (11, 12); (–11, –12); (–11, 12); (–12, 11); (10, 10); (10, 5)'  + '\n' + '\n' + 'Сколько было запусков, при которых программа напечатала «ДА»?')
        bot.send_message(message.chat.id,  f'Ответ: ||3||', parse_mode='MarkdownV2',  reply_markup=markup2) 
        
    # 2 ВАРИАНТ. ЗАДАНИЕ №7
    elif message.text == '⏩ Следующее задание. В2-7':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В2-8')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=1qHXzmYnO7A")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №7.',  reply_markup=markup)
        bot.send_message(message.chat.id, 'Доступ к файлу page.htm, находящемуся на сервере book.ru, осуществляется по протоколу http. В таблице фрагменты адреса файла закодированы цифрами от 1 до 7. Запишите последовательность этих цифр, кодирующую адрес указанного файла в сети Интернет.'  + '\n' + '\n' + '1) /'  + '\n' + '2) page'  + '\n' + '3) ://'  + '\n' + '4) .ru'  + '\n' + '5) .htm'  + '\n' + '6) book'  + '\n' + '7) http')
        bot.send_message(message.chat.id,  f'Ответ: ||7364125||', parse_mode='MarkdownV2',  reply_markup=markup2) 

    # 2 ВАРИАНТ. ЗАДАНИЕ №8
    elif message.text == '⏩ Следующее задание. В2-8':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В2-9')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=xxxI27oFs1E")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №8.',  reply_markup=markup)
        bot.send_message(message.chat.id, 'Ниже приведены запросы и количество страниц, которые нашел поисковый сервер по этим запросам в некотором сегменте Интернета:' + '\n' + '\n' + 'фрегат | эсминец    3000' + '\n' + 'фрегат                       2000' + '\n' + 'эсминец                    2500' + '\n' + '\n' + 'Сколько страниц будет найдено по запросу: фрегат & эсминец ?')
        bot.send_message(message.chat.id,  f'Ответ: ||1500||', parse_mode='MarkdownV2',  reply_markup=markup2)

    # 2 ВАРИАНТ. ЗАДАНИЕ №9
    elif message.text == '⏩ Следующее задание. В2-9':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В2-10')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=Xrjl7lv3sVM")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №9.',  reply_markup=markup)
        bot.send_message(message.chat.id, 'На рисунке – схема дорог, связывающих города А, Б, В, Г, Д, Е, Ж, З, И, К и Л. По каждой дороге можно двигаться только в одном направлении, указанном стрелкой. Сколько существует различных путей из города А в город Л, проходящих через город В?')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B2-9.png?raw=true')
        bot.send_message(message.chat.id,  f'Ответ: ||10||', parse_mode='MarkdownV2',  reply_markup=markup2)
 
    # 2 ВАРИАНТ. ЗАДАНИЕ №10
    elif message.text == '⏩ Следующее задание. В2-10':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В2-11')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=HNXq5tJS8Fg")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №10.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'Среди приведённых ниже трёх чисел, записанных в различных системах счисления, найдите максимальное и запишите его в ответе в десятичной системе счисления. В ответе запишите только число, основание системы счисления указывать не нужно.')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B2-10.png?raw=true')
        bot.send_message(message.chat.id,  f'Ответ: ||43||', parse_mode='MarkdownV2',  reply_markup=markup2) 
 
    # 2 ВАРИАНТ. ЗАДАНИЕ №11
    elif message.text == '⏩ Следующее задание. В2-11':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В2-12')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="🗂️ Архив", url="https://drive.google.com/file/d/1fol9PPO1X7Tk-sYJbNbUP0k985ynhgWw/view?usp=share_link")
        url_button2 = types.InlineKeyboardButton(text="☁️ Облако", url="https://drive.google.com/drive/folders/15ODP0Xbh44gkUBmO-6ZEsZc1Yzasvk8u?usp=share_link")
        url_button3 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=7HfOEFw2K8g")
        markup3 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(url_button1,url_button2)
        markup3.add(url_button3)
        bot.send_message(message.chat.id, 'Задание №11.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'В одном из произведений И.С. Тургенева, текст которого приведён в подкаталоге Тургенев, встречается m-lle Boncourt. С помощью поисковых средств операционной системы и текстового редактора выясните, сколько примерно лет было m-lle Boncourt.',  reply_markup=markup2)
        bot.send_message(message.chat.id,  f'Ответ: ||60||', parse_mode='MarkdownV2',  reply_markup=markup3) 
 
    # 2 ВАРИАНТ. ЗАДАНИЕ №12
    elif message.text == '⏩ Следующее задание. В2-12':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В2-13-1')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="🗂️ Архив", url="https://drive.google.com/file/d/1-mtQfHG66RNkrUwUmhKvh9vZWIANImBM/view?usp=share_link")
        url_button2 = types.InlineKeyboardButton(text="☁️ Облако", url="https://drive.google.com/drive/folders/1o3JRUvnxghkdUydgHOJZ1uYBGcUALlLt?usp=share_link")
        url_button3 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=0DZw0af1cNE")
        markup3 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(url_button1,url_button2)
        markup3.add(url_button3)
        bot.send_message(message.chat.id, 'Задание №12.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'Определите наибольший размер файла в килобайтах среди файлов с расширением .txt в подкаталогах каталога Поэзия? В ответе укажите только число.',  reply_markup=markup2)
        bot.send_message(message.chat.id,  f'Ответ: ||50||', parse_mode='MarkdownV2',  reply_markup=markup3) 
 
    # 2 ВАРИАНТ. ЗАДАНИЕ №13-1
    elif message.text == '⏩ Следующее задание. В2-13-1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В2-13-2')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="🗂️ Архив", url="https://drive.google.com/file/d/1uxeAbGMK0ejYWSU68hngQkvwGoR8ek3G/view?usp=share_link")
        url_button2 = types.InlineKeyboardButton(text="☁️ Облако", url="https://drive.google.com/drive/folders/1dqb7HYX5gjd-K1XH1du2sHVrRrA5tnfn?usp=share_link")
        url_button3 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=MYQaEc0FuMc")
        markup3 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(url_button1,url_button2,url_button3)
        bot.send_message(message.chat.id, 'Задание №13-1.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'Распакуйте архив irbis.zip. Используя информацию и иллюстративный материал, содержащийся в файлах архива, создайте презентацию из трёх слайдов на тему «Снежный барс». В презентации должны содержаться краткие иллюстрированные сведения о внешнем виде, ареале обитания и образе жизни снежных барсов (ирбисов). Все слайды должны быть выполнены в едином стиле, каждый слайд должен быть озаглавлен. В презентации должен использоваться единый тип шрифта.' + '\n' + '\n' + 'Требования к оформлению презентации:' + '\n' + '1.	Параметры страницы (слайда): экран (16:9), ориентация альбомная.' + '\n' + '2.	Первый слайд – титульный слайд с названием презентации, в подзаголовке титульного слайда в качестве информации об авторе презентации указывается идентификационный номер участника экзамена.'  + '\n' + '3.	Второй слайд – основная информация в соответствии с заданием, размещённая по образцу на рисунке макета слайда 2: заголовок слайда; два блока текста; два изображения.'  + '\n' + '4.	Третий слайд – дополнительная информация по теме презентации, размещённая по образцу на рисунке макета слайда 3: заголовок слайда; три изображения; три блока текста.'  + '\n' + '5.	Размер шрифта: для названия презентации на титульном слайде – 40 пунктов; для подзаголовка на титульном слайде и заголовков слайдов – 24 пункта; для подзаголовков на втором и третьем слайдах и для основного текста – 20 пунктов. Текст не должен перекрывать основные изображения или сливаться с фоном.')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B2-13-1.png?raw=true',  reply_markup=markup2)
 
    # 2 ВАРИАНТ. ЗАДАНИЕ №13-2
    elif message.text == '⏩ Следующее задание. В2-13-2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В2-14')
        markup.add(btn1, btn2)
        markup.row(back)
        url_button3 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=CvACQFXx7GA&t=13s")
        markup3 = types.InlineKeyboardMarkup(row_width=1)
        markup3.add(url_button3)
        bot.send_message(message.chat.id, 'Задание №13-2.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'Создайте в текстовом редакторе документ и напишите в нём следующий текст, точно воспроизведя всё оформление текста, имеющееся в образце. Данный текст должен быть написан шрифтом размером 14 пунктов. Основной текст выровнен по ширине, и первая строка абзаца имеет отступ 1 см. В тексте есть слова, выделенные жирным шрифтом, курсивом и подчёркиванием.' + '\n' + 'При этом допустимо, чтобы ширина Вашего текста отличалась от ширины текста в примере, поскольку ширина текста зависит от размера страницы и полей. В этом случае разбиение текста на строки должно соответствовать стандартной ширине абзаца.')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B2-13-2.png?raw=true',  reply_markup=markup3)
 
    # 2 ВАРИАНТ. ЗАДАНИЕ №14
    elif message.text == '⏩ Следующее задание. В2-14':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В2-15-1')
        markup.add(btn1, btn2)
        markup.row(back)
        url_button3 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=Oh3ijrnQ850")
        markup3 = types.InlineKeyboardMarkup(row_width=1)
        markup3.add(url_button3)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button2 = types.InlineKeyboardButton(text="☁️ Облако", url="https://docs.google.com/spreadsheets/d/1xHSSAaGRBPzOTX4cE7xPU5vbwfzMMqLY/edit?usp=share_link&ouid=104878964026869489773&rtpof=true&sd=true")
        markup2.add(url_button2)
        bot.send_message(message.chat.id, 'Задание №14.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'В электронную таблицу занесли данные о тестировании учеников по выбранным ими предметам. В столбце A записан код округа, в котором учится ученик; в столбце B – фамилия; в столбце C – выбранный учеником предмет; в столбце D – тестовый балл. Всего в электронную таблицу были занесены данные 1000 учеников.') 
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B2-14.png?raw=true')
        bot.send_message(message.chat.id, 'На основании данных, содержащихся в этой таблице, выполните задания.'  + '\n' + '1. Определите, сколько учеников, которые проходили тестирование по физкультура, набрали более 200 баллов. Ответ запишите в ячейку H2 таблицы.'  + '\n' + '2. Найдите средний тестовый балл учеников, которые проходили тестирование по физкультуре. Ответ запишите в ячейку H3 таблицы с точностью не менее двух знаков после запятой.'  + '\n' + '3. Постройте круговую диаграмму, отображающую соотношение числа участников из округов с кодами «C», «ЮЗ» и «З». Левый верхний угол диаграммы разместите вблизи ячейки G6.',  reply_markup=markup2) 
        bot.send_message(message.chat.id,  f'Ответ:\n||1\) 172 \n2\) 458,03 \n3\) C\-66; ЮЗ\-223; З\-108||', parse_mode='MarkdownV2',  reply_markup=markup3) 
 
    # 2 ВАРИАНТ. ЗАДАНИЕ №15-1
    elif message.text == '⏩ Следующее задание. В2-15-1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В2-15-2')
        markup.add(btn1, btn2)
        markup.row(back)
        url_button3 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=Oh3ijrnQ850")
        markup3 = types.InlineKeyboardMarkup(row_width=1)
        markup3.add(url_button3)
        bot.send_message(message.chat.id, 'Задание №15-1.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'На бесконечном поле есть горизонтальная и вертикальная стены. Левый конец горизонтальной стены соединён с верхним концом вертикальной стены. Длины стен неизвестны. В каждой стене есть ровно один проход, точное место прохода и его ширина неизвестны. Робот находится в клетке, расположенной непосредственно справа от вертикальной стеной у её нижнего конца.') 
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B2-15-1.png?raw=true')
        bot.send_message(message.chat.id, 'Напишите для Робота алгоритм, закрашивающий все клетки, расположенные непосредственно ниже горизонтальной стены и правее вертикальной стены, кроме клетки, в которой находится Робот перед выполнением программы.') 
        bot.send_message(message.chat.id,  f"Ответ: \n||вверх\nнц пока не слева свободно\n  закрасить\n  вверх\nкц\nнц пока слева свободно\n  вверх\nкц\nнц пока сверху свободно\n  закрасить\n  вверх\nкц\nнц пока не сверху свободно\n  закрасить\n  вправо\nкц\nнц пока сверху свободно\n  вправо\nкц\nнц пока не сверху свободно\n  закрасить\n  вправо\nкц||", parse_mode='MarkdownV2',  reply_markup=markup3) 
 
    # 2 ВАРИАНТ. ЗАДАНИЕ №15-2
    elif message.text == '⏩ Следующее задание. В2-15-2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        markup.add(btn1)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=tJw3fjAOCII")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №15-2.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'Напишите программу, которая в последовательности натуральных чисел находит среднее арифметическое чисел, кратных 8, или сообщает, что таких чисел нет (выводит «NO»). Программа получает на вход натуральные числа, количество введённых чисел неизвестно, последовательность чисел заканчивается числом 0 (0 – признак окончания ввода, не входит в последовательность). Количество чисел не превышает 100. Введённые числа не превышают 300. Программа должна вывести среднее арифметическое чисел, кратных 8, или вывести «NO», если таких чисел нет. Значение выводить с точностью до десятых.' + '\n' + 'Пример работы программы:')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B2-15-2.png?raw=true')
        bot.send_message(message.chat.id,  f'Ответ:\n||var a, s, n: integer;\nbegin\n  s:\=0; n:\=0;\n  readln\(a\);\n  while a\<\>0 do begin\n    if \(a mod 8 \= 0\) then begin\n      s :\= s \+ a;\n      n :\= n \+ 1;\n    end;\n    readln\(a\); \n  end;\n  if n \> 0 then \n       writeln\(s\/n :5:1\)\n  else writeln\(\'NO\'\);\nend\.||', parse_mode='MarkdownV2',  reply_markup=markup2) 
    # 3 ВАРИАНТ       
    # 3 ВАРИАНТ
    # 3 ВАРИАНТ
    # 3 ВАРИАНТ        
    # 3 ВАРИАНТ
    # 3 ВАРИАНТ. ЗАДАНИЕ №1
    elif message.text == '📙 Вариант №3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В3-2')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=9H9xAK3Y25o")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №1.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'В одной из кодировок Unicode каждый символ кодируется 16 битами. Вова написал текст (в нём нет лишних пробелов):' + '\n' + '\n' + '«Собака, кошка, курица, корова, лошадь, коза, овца – домашние животные».' + '\n' + '\n' + 'Затем он добавил в список название ещё одного животного. Заодно он добавил необходимые запятые и пробелы. При этом размер нового предложения в данной кодировке оказался на 10 байт больше, чем размер исходного предложения. Напишите в ответе длину добавленного названия животного в символах.') 
        bot.send_message(message.chat.id,  f'Ответ: ||Курица||', parse_mode='MarkdownV2',  reply_markup=markup2)

    # 3 ВАРИАНТ. ЗАДАНИЕ №2
    elif message.text == '⏩ Следующее задание. В3-2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В3-3')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=CEtG5MUmvWM")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №2.',  reply_markup=markup)
        bot.send_message(message.chat.id, 'От разведчика было получено сообщение:'  + '\n' + '\n' + '1010111110010001111' + '\n' + '\n' +  'В этом сообщении зашифрован пароль – последовательность русских букв. В пароле использовались только буквы А, Б, К, Л, О, С; каждая буква кодировалась двоичным словом по таблице, показанной на рисунке. Расшифруйте сообщение. Запишите в ответе пароль.')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B3-2.png?raw=true')
        bot.send_message(message.chat.id,  f'Ответ: ||ксбоалб||', parse_mode='MarkdownV2',  reply_markup=markup2)
 
    # 3 ВАРИАНТ. ЗАДАНИЕ №3
    elif message.text == '⏩ Следующее задание. В3-3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В3-4
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://youtu.be/Ekrt54b_8as")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №3.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'Напишите наибольшее целое число x, для которого истинно высказывание:' + '\n' + '\n' + '(x < 25) И НЕ (x делится на 8)')
        bot.send_message(message.chat.id,  f'Ответ: ||23||', parse_mode='MarkdownV2',  reply_markup=markup2) 

    # 3 ВАРИАНТ. ЗАДАНИЕ №4
    elif message.text == '⏩ Следующее задание. В3-4':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В3-5')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=8lv-35Y1yQY")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №4.',  reply_markup=markup)
        bot.send_message(message.chat.id, 'Между населёнными пунктами A, B, C, D, E, F построены дороги, протяжённость которых приведена в таблице. Отсутствие числа в таблице означает, что прямой дороги между пунктами нет. Определите длину кратчайшего пути между пунктами A и E, проходящего через пункт D. Передвигаться можно только по указанным дорогам.')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B3-4.png?raw=true')
        bot.send_message(message.chat.id,  f'Ответ: ||9||', parse_mode='MarkdownV2',  reply_markup=markup2) 
        
    # 3 ВАРИАНТ. ЗАДАНИЕ №5
    elif message.text == '⏩ Следующее задание. В3-5':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В3-6')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=ybwyb-CdNTg")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №5.',  reply_markup=markup)
        bot.send_message(message.chat.id, 'У исполнителя Альфа две команды, которым присвоены номера:' + '\n' + '\n' + '1. прибавь 1' + '\n' + '2. умножь на b' + '\n' + '\n' + 'b - неизвестное натуральное число; b ≥ 2) Выполняя первую из них, Альфа увеличивает число на экране на 1, а выполняя вторую, умножает это число на b. Известно, что программа 11221 переводит число 5 в число 176. Определите значение b.') 
        bot.send_message(message.chat.id,  f'Ответ: ||5||', parse_mode='MarkdownV2',  reply_markup=markup2)
        
    # 3 ВАРИАНТ. ЗАДАНИЕ №6
    elif message.text == '⏩ Следующее задание. В3-6':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В3-7')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=R2upK0ujKaQ")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №6.',  reply_markup=markup)
        bot.send_message(message.chat.id, 'Дана программа:')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B3-6.png?raw=true')
        bot.send_message(message.chat.id, 'Было проведено 9 запусков программы, при которых в качестве значений переменных s и t вводились следующие пары чисел:' + '\n' + '\n' + '(15, 25); (15, 10); (20, 5); (25, 10); (30, 10); (10, 10); (20, 20); (15, 5); (20, 10); (10, 20)'  + '\n' + '\n' + 'Сколько было запусков, при которых программа напечатала «ДА»?')
        bot.send_message(message.chat.id,  f'Ответ: ||3||', parse_mode='MarkdownV2',  reply_markup=markup2) 
        
    # 3 ВАРИАНТ. ЗАДАНИЕ №7
    elif message.text == '⏩ Следующее задание. В3-7':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В3-8')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=1qHXzmYnO7A")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №7.',  reply_markup=markup)
        bot.send_message(message.chat.id, 'Доступ к файлу home.jpg, находящемуся на сервере travels.ru, осуществляется по протоколу http. Фрагменты адреса файла закодированы цифрами от 1 до 7. Запишите последовательность этих цифр, кодирующую адрес указанного файла в сети Интернет.'  + '\n' + '\n' + '1) .jpg'  + '\n' + '2) http'  + '\n' + '3) ://'  + '\n' + '4) /'  + '\n' + '5) home'  + '\n' + '6) ru'  + '\n' + '7) travels.')
        bot.send_message(message.chat.id,  f'Ответ: ||2376451||', parse_mode='MarkdownV2',  reply_markup=markup2) 

    # 3 ВАРИАНТ. ЗАДАНИЕ №8
    elif message.text == '⏩ Следующее задание. В3-8':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В3-9')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=xxxI27oFs1E")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №8.',  reply_markup=markup)
        bot.send_message(message.chat.id, 'Ниже приведены запросы и количество страниц, которые нашел поисковый сервер по этим запросам в некотором сегменте Интернета:' + '\n' + '\n' + 'Пушкин | Лермонтов     5200' + '\n' + 'Пушкин & Лермонтов   300' + '\n' + 'Лермонтов                     2100' + '\n' + '\n' + 'Сколько страниц будет найдено по запросу: Пушкин ?')
        bot.send_message(message.chat.id,  f'Ответ: ||3400||', parse_mode='MarkdownV2',  reply_markup=markup2)

    # 3 ВАРИАНТ. ЗАДАНИЕ №9
    elif message.text == '⏩ Следующее задание. В3-9':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В3-10')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=Xrjl7lv3sVM")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №9.',  reply_markup=markup)
        bot.send_message(message.chat.id, 'На рисунке – схема дорог, связывающих города A, B, C, D, E и F. По каждой дороге можно двигаться только в одном направлении, указанном стрелкой. Сколько существует различных путей из города A в город F, не проходящих через город Е?')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B3-9.png?raw=true')
        bot.send_message(message.chat.id,  f'Ответ: ||3||', parse_mode='MarkdownV2',  reply_markup=markup2)
 
    # 3 ВАРИАНТ. ЗАДАНИЕ №10
    elif message.text == '⏩ Следующее задание. В3-10':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В3-11')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=HNXq5tJS8Fg")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №10.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'Среди приведённых ниже трёх чисел, записанных в различных системах счисления, найдите минимальное и запишите его в ответе в десятичной системе счисления. В ответе запишите только число, основание системы счисления указывать не нужно.')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B3-10.png?raw=true')
        bot.send_message(message.chat.id,  f'Ответ: ||52||', parse_mode='MarkdownV2',  reply_markup=markup2) 
 
    # 3 ВАРИАНТ. ЗАДАНИЕ №11
    elif message.text == '⏩ Следующее задание. В3-11':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В3-12')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="🗂️ Архив", url="https://drive.google.com/file/d/1_LUw_WBTQbGlmnYtc_Y1Zfqx38YpoPhJ/view?usp=share_link")
        url_button2 = types.InlineKeyboardButton(text="☁️ Облако", url="https://drive.google.com/drive/folders/1BaoYYJcZb8Tn7yD4W9x4VASVkrw9ZF2l?usp=share_link")
        url_button3 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=7HfOEFw2K8g")
        markup3 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(url_button1,url_button2)
        markup3.add(url_button3)
        bot.send_message(message.chat.id, 'Задание №11.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'В одном из произведений И.С. Тургенева, текст которого приведён в подкаталоге Тургенев (архив oge12.zip), одного из героев зовут Волынцев. С помощью поисковых средств операционной системы и текстового редактора выясните название пруда, у которого девушка назначила свидание главному герою.',  reply_markup=markup2)
        bot.send_message(message.chat.id,  f'Ответ: ||Авдюхин||', parse_mode='MarkdownV2',  reply_markup=markup3) 
 
    # 3 ВАРИАНТ. ЗАДАНИЕ №12
    elif message.text == '⏩ Следующее задание. В3-12':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В3-13')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="🗂️ Архив", url="https://drive.google.com/file/d/1rlBEx4eXKx7VY2OrEoJq2py9SBNlbw7m/view?usp=share_link")
        url_button2 = types.InlineKeyboardButton(text="☁️ Облако", url="https://drive.google.com/drive/folders/1Q0jOF2P4J-YMHnC8uuE9XAnjNr2UhCXJ?usp=share_link")
        url_button3 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=0DZw0af1cNE")
        markup3 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(url_button1,url_button2)
        markup3.add(url_button3)
        bot.send_message(message.chat.id, 'Задание №12.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'Определите наименьший размер файла в килобайтах среди файлов с расширением .pdf в подкаталогах каталога Проза (архив oge12.zip)? В ответе укажите только число.',  reply_markup=markup2)
        bot.send_message(message.chat.id,  f'Ответ: ||217||', parse_mode='MarkdownV2',  reply_markup=markup3) 
 
    # 3 ВАРИАНТ. ЗАДАНИЕ №13
    elif message.text == '⏩ Следующее задание. В3-13':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В3-14')
        markup.add(btn1, btn2)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="🗂️ Архив", url="https://drive.google.com/file/d/1uxeAbGMK0ejYWSU68hngQkvwGoR8ek3G/view?usp=share_link")
        url_button2 = types.InlineKeyboardButton(text="☁️ Облако", url="https://drive.google.com/drive/folders/1dqb7HYX5gjd-K1XH1du2sHVrRrA5tnfn?usp=share_link")
        url_button3 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=MYQaEc0FuMc")
        markup3 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(url_button1,url_button2,url_button3)
        bot.send_message(message.chat.id, 'Задание №13.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'Создайте в текстовом редакторе документ и напишите в нём следующий текст, точно воспроизведя всё оформление текста, имеющееся в образце. Данный текст должен быть написан шрифтом размером 14 пунктов. ' + '\n' + 'Основной текст выровнен по ширине, и первая строка абзаца имеет отступ 1 см. В тексте есть слова, выделенные жирным шрифтом, курсивом и подчёркиванием.' + '\n' + 'При этом допустимо, чтобы ширина Вашего текста отличалась от ширины текста в примере, поскольку ширина текста зависит от размера страницы и полей. В этом случае разбиение текста на строки должно соответствовать стандартной ширине абзаца.')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B3-13.png?raw=true',  reply_markup=markup2)
 
    # 3 ВАРИАНТ. ЗАДАНИЕ №14
    elif message.text == '⏩ Следующее задание. В3-14':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В3-15-1')
        markup.add(btn1, btn2)
        markup.row(back)
        url_button3 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=Oh3ijrnQ850")
        markup3 = types.InlineKeyboardMarkup(row_width=1)
        markup3.add(url_button3)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button2 = types.InlineKeyboardButton(text="☁️ Облако", url="https://docs.google.com/spreadsheets/d/1xHSSAaGRBPzOTX4cE7xPU5vbwfzMMqLY/edit?usp=share_link&ouid=104878964026869489773&rtpof=true&sd=true")
        markup2.add(url_button2)
        bot.send_message(message.chat.id, 'Задание №14.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'В электронную таблицу занесли результаты тестирования учащихся по различным предметам. На рисунке приведены первые строки получившейся таблицы. Всего в электронную таблицу были занесены данные по 1000 учащимся. Порядок записей в таблице произвольный. Число 0 в таблице означает, что ученик не сдавал соответствующий экзамен.') 
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B3-14.png?raw=true')
        bot.send_message(message.chat.id, 'На основании данных, содержащихся в этой таблице, выполните задания.'  + '\n' + '1. Сколько учеников сдали экзамен по математике на отметку 4 или 5 баллов, а на экзамене по иностранному языку получили отметку ниже, чем 4 балла? Ответ на этот вопрос запишите в ячейку H2 таблицы.'  + '\n' + '2. Каков средний балл учеников 7 класса по математике? Учтите, что некоторые ученики не сдавали этот экзамен. Ответ с точностью до двух знаков после запятой запишите в ячейку H3 таблицы.'  + '\n' + '3. Постройте круговую диаграмму, отображающую соотношение числа учеников 5, 6 и 8 классов, присутствующих в списке. Левый верхний угол диаграммы разместите вблизи ячейки G6.',  reply_markup=markup2) 
        bot.send_message(message.chat.id,  f'Ответ:\n||1\) 161 \n2\) 2,81 \n3\) 5\-105; 6\-99; 8\-84||', parse_mode='MarkdownV2',  reply_markup=markup3) 
 
    # 3 ВАРИАНТ. ЗАДАНИЕ №15-1
    elif message.text == '⏩ Следующее задание. В3-15-1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        btn2 = types.KeyboardButton('⏩ Следующее задание. В3-15-2')
        markup.add(btn1, btn2)
        markup.row(back)
        url_button3 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=Oh3ijrnQ850")
        markup3 = types.InlineKeyboardMarkup(row_width=1)
        markup3.add(url_button3)
        bot.send_message(message.chat.id, 'Задание №15-1.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'На бесконечном поле есть горизонтальная и вертикальная стены. Левый конец горизонтальной стены соединён с нижним концом вертикальной стены. Длины стен неизвестны. В каждой стене есть ровно один проход, точное место прохода и его ширина неизвестны. Робот находится в клетке, расположенной непосредственно сверху над горизонтальной стеной у правого конца прохода.') 
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B3-15-1.png?raw=true')
        bot.send_message(message.chat.id, 'Напишите для Робота алгоритм, закрашивающий все клетки, расположенные непосредственно выше горизонтальной стены и правее вертикальной стены, кроме клетки, в которой находится Робот перед выполнением программы.') 
        bot.send_message(message.chat.id,  f"Ответ:\n||вправо\nнц пока не снизу свободно\n  закрасить\n  вправо\nкц\nвлево\nнц пока не cнизу свободно\n  влево\nкц\nнц пока снизу свободно\n  влево\nкц\nнц пока слева свободно\n  закрасить\n  влево\nкц\nнц пока не слева свободно\n  закрасить\n  вверх\nкц\nнц пока слева свободно\n  вверх\nкц\nнц пока не слева свободно\n  закрасить\n  вверх\nкц||", parse_mode='MarkdownV2',  reply_markup=markup3) 
 
    # 3 ВАРИАНТ. ЗАДАНИЕ №15-2
    elif message.text == '⏩ Следующее задание. В3-15-2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('❇️ Главное меню')
        btn1 = types.KeyboardButton('📝 Перейти к заданиям')
        markup.add(btn1)
        markup.row(back)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="📺 Видео-разбор", url="https://www.youtube.com/watch?v=tJw3fjAOCII")
        markup2.add(url_button1)
        bot.send_message(message.chat.id, 'Задание №15-2.',  reply_markup=markup) 
        bot.send_message(message.chat.id, 'Напишите программу, которая в последовательности натуральных чисел определяет сумму чисел, кратных 3 и оканчивающихся на 4. Программа получает на вход количество чисел в последовательности, а затем сами числа. В последовательности всегда имеется число, кратное 3 и оканчивающееся на 4. Количество чисел не превышает 100. Введённые числа по модулю не превышают 300. Программа должна вывести одно число: сумму чисел, кратных 3 и оканчивающихся на 4. Пример работы программы:')
        bot.send_photo(message.chat.id, 'https://github.com/1337Roly2/school2087/blob/main/pics/B3-15-2.png?raw=true')
        bot.send_message(message.chat.id,  f'Ответ:\n||var n,i,a,s: integer;\nbegin\n  readln\(n\);\n  s :\= 0;\n  for i :\= 1 to n do begin\n    readln\(a\);\n    if \(a mod 3 \= 0\) and\(a mod 10 \= 4\)\n      then s :\= s \+ a;\n  end;\n  writeln\(s\)\nend\.||', parse_mode='MarkdownV2',  reply_markup=markup2) 
 
bot.polling(none_stop=True, interval=0)
