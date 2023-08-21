import telebot
import os
from telebot import types

# Как предложение у тебя папки с изображениями называются мальчик и девочка, я бы предложил другую структуры
# data -> img и text -> text_ru, text_en, img_boy, img_girl
# И ты будешь знать и кто-то другой будет знать, что в данных хранятся текст и изображения которые используются в твоем боте

# Попробуй вынести токен в отдельный файл, например назови его config или setings, можешь его сделать без формата, а можешь сделать .ini
# например config.ini, а в нем указать:
# token: 6474703393:AAE8JBaernftP0-SElrKPQU8wOyadjT49v0
# а как его прочитать, то можешь посмотреть парсеры настроек или парсеры конфиг файлов в python
token = "6474703393:AAE8JBaernftP0-SElrKPQU8wOyadjT49v0"
bot = telebot.TeleBot(token)

# если у тебя не будет этой папки в проекте, то программа сломается, можно сделать тсключение, чтобы не ломалась
# а можно попробовать вариант, что программа смотрит, есть ли такая папка, если её нет, то срабатывает исключение
# и при сработке данного исключения она создает нужную папку по нужному пути
females = os.listdir('./girl')
male = os.listdir('./boy')

#  В данном пути вторая точка не нужна, точка указывает на то, что путь не абсолютный, а корнем является папка откуда ты запускаешь свой файл
# ./girl_text/girl.text1.txt

# И вопрос стоит ла открывать на чтение и помещать в память так много файлов
# Можно попробовать создать один файл, а в нем по опредленным тегам сделать разбитие
# примерно как по аналогии с настройками, но это на подумать здесь конечно, как тебе удобнее
# но все опреации на чтение и запись файлов или вывод и ввод в консоль информации, занимают много времени так как выполняются через сигналы прерывания

# Это не побуждение к действиям просто на подумать, прохождение по шести файлам, можно как вариант разбить на девочки и пустить чтение трех файлов в цикле и по подобию на мальчики
with open('./girl_text./girl.text1.txt') as k :
    one_girl_cats = open('./girl_text./girl.text1.txt').read()


# Не забывай пока не начались классы или в функции в твоем коде, то делай всегда два отступа, хороший тон для чтения кода
with open('./girl_text./girl.text2.txt') as k:
    two_girl_cats = open('./girl_text./girl.text2.txt').read()


with open('./girl_text./girl.text3.txt') as k:
    three_girl_cats = open('./girl_text./girl.text3.txt').read()


with open('./boy_text./boy_text1.txt') as k:
    one_boy_cats = open('./boy_text./boy_text1.txt').read()


with open('./boy_text./boy_text2.txt') as k:
    two_boy_cats = open('./boy_text./boy_text2.txt').read()


with open('./boy_text./boy_text3.txt') as k:
    three_boy_cats = open('./boy_text./boy_text3.txt').read()

# если ты верхнее сделаешь в цикле, то ты тогда сможешь сразу это добавить в список при прохождении через функцию append
# код сократиться и будет более читабельнее
boy_text_cats = [one_boy_cats,two_boy_cats,three_boy_cats]
girl_text_cats = [one_girl_cats,two_girl_cats,three_girl_cats]

# Про разделения русского и англиского я еще подумаю, как лучше сделать, может и такой вариант будет лучшим
females_en = os.listdir('./girl_en')
male_en = os.listdir('./boy_en')


@bot.message_handler(commands=['start'])
def start_handler(message):
    # Попробуй если будет время добавить к каждой функции краткое описание, как сам ты видишь
    # просто бывает такое, что в проекте участвует целая команда и она увидит твой код в первый раз и начнет разбираться
    # а если будет описание функций или классов она быстрее найдет, то что ей необходимо посмотреть или то, что ты бы хотел, чтобы кто-то посмотрел
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Русский",callback_data='ru')
    btn2 = types.InlineKeyboardButton("English", callback_data='en')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, '<b> 😽Пожалуйста,выберите язык. </b>  \n'
                                      '<b> Please select a language.😽 </b>', reply_markup=markup, parse_mode='html')

# Все ситуации я посмтрю завтра более детально, думаю можно как-то будет вынести в отдельную переменную язык и разветвление сделать чуть меньше и проще
# просто код полностью дублируется, а можно же проверять переменную lang и смотреть если англиский, то тодно выводить если наш РУССКИЙ, то другие
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global male_en, females_en,girl_text_cats
    # постарайся преименовать и не давать такие названия переменным как i или j переменным, через несколько месяцев ты сам посмотришь на код и не поймешь, что же ты перебирал в данном цикле
    # ну и другим пользователям кто увидит твой код будет более понятнее

    for j in females_en:
        if call.data == j:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            bot.send_photo(call.message.chat.id, photo=open(f'''./girl_en/{j}''', 'rb'))
            markup = types.InlineKeyboardMarkup(row_width=1)

            if females_en.index(j) + 1 > len(females_en) - 1:
                btn9 = types.InlineKeyboardButton("📝buy", callback_data='buy_en')
                btn7 = types.InlineKeyboardButton("◀️back", callback_data=females_en[females_en.index(j) - 1])
                btn8 = types.InlineKeyboardButton("◀️️To main menu", callback_data='back_to_main_page_cats_en')
                markup.add(btn9,btn7, btn8)

            elif females_en.index(j) == 0:
                btn7 = types.InlineKeyboardButton("📝buy", callback_data="buy_en")
                btn9 = types.InlineKeyboardButton("▶️Further", callback_data=females_en[females_en.index(j) + 1])
                btn8 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page_cats_en')
                markup.add(btn7, btn9, btn8)
                bot.send_message(chat_id=call.message.chat.id, text=girl_text_cats[0], reply_markup=markup)
                bot.delete_message(call.message.chat.id, call.message.message_id)

            else:
                btn7 = types.InlineKeyboardButton("▶️Further", callback_data=females_en[females_en.index(j) + 1])
                btn9 = types.InlineKeyboardButton("📝buy", callback_data='buy_en')
                btn10 = types.InlineKeyboardButton("◀️back", callback_data=females_en[females_en.index(j) - 1])
                btn8 = types.InlineKeyboardButton("◀️️To main menu", callback_data='back_to_main_page_cats_en')
                markup.add(btn9,btn7,btn10,btn8)
                bot.send_message(chat_id=call.message.chat.id, text=boy_text_cats[1], reply_markup=markup)
            bot.send_message(chat_id=call.message.chat.id, text=girl_text_cats[-1], reply_markup=markup)

    for i in male_en:
        if call.data == i:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            bot.send_photo(call.message.chat.id, photo=open(f'''./boy_en/{i}''', 'rb'))
            markup = types.InlineKeyboardMarkup(row_width=1)

            if male_en.index(i) + 1 > len(male_en) - 1:
                btn9 = types.InlineKeyboardButton("📝buy", callback_data='buy_en')
                btn7 = types.InlineKeyboardButton("◀️back", callback_data=male_en[male_en.index(i) - 1])
                btn8 = types.InlineKeyboardButton("◀️️To main menu", callback_data='back_to_main_page_cats_en')
                markup.add(btn9,btn7, btn8)

            elif male_en.index(i) == 0:
                btn7 = types.InlineKeyboardButton("📝buy", callback_data="buy_en")
                btn9 = types.InlineKeyboardButton("▶️Further", callback_data=male_en[male_en.index(i) + 1])
                btn8 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page_cats_en')
                markup.add(btn7, btn9, btn8)
                bot.send_message(chat_id=call.message.chat.id, text=boy_text_cats[0], reply_markup=markup)
                bot.delete_message(call.message.chat.id, call.message.message_id)

            else:
                btn10 = types.InlineKeyboardButton("📝buy", callback_data='buy_en')
                btn8 = types.InlineKeyboardButton("◀️back", callback_data=male_en[male_en.index(i) - 1])
                btn7 = types.InlineKeyboardButton("▶️Further", callback_data=male_en[male_en.index(i) + 1])
                btn9 = types.InlineKeyboardButton("◀️️To main menu", callback_data='back_to_main_page_cats_en')
                markup.add(btn10,btn7,btn8,btn9)
                bot.send_message(chat_id=call.message.chat.id, text=boy_text_cats[1], reply_markup=markup)
            bot.send_message(chat_id=call.message.chat.id, text=boy_text_cats[-1], reply_markup=markup)

    for i in females:
        if call.data == i:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            bot.send_photo(call.message.chat.id, photo=open(f'''./girl/{i}''', 'rb'))
            markup = types.InlineKeyboardMarkup(row_width=1)

            if females.index(i) + 1 > len(females) - 1:
                btn9 = types.InlineKeyboardButton("📝Купить", callback_data='buy')
                btn10 = types.InlineKeyboardButton("◀️Назад", callback_data= females[females.index(i) - 1])
                btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page_kittens')
                markup.add(btn9,btn10,btn8)

            elif females.index(i) == 0:
                btn7 = types.InlineKeyboardButton("▶️Далее", callback_data=females[females.index(i) + 1])
                btn9 = types.InlineKeyboardButton("📝Купить", callback_data='buy')
                btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page_kittens')
                markup.add(btn7, btn9, btn8)
                bot.send_message(chat_id=call.message.chat.id, text=girl_text_cats[0], reply_markup=markup)
                bot.delete_message(call.message.chat.id, call.message.message_id)

            else:
                btn10 = types.InlineKeyboardButton("◀️Назад", callback_data=females[females.index(i) - 1])
                btn7 = types.InlineKeyboardButton("▶️Далее", callback_data=females[females.index(i) + 1])
                btn9 = types.InlineKeyboardButton("📝Купить", callback_data='buy')
                btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page_kittens')
                markup.add(btn9, btn7, btn10,btn8)
                bot.send_message(chat_id=call.message.chat.id, text=girl_text_cats[1], reply_markup=markup)
            bot.send_message(chat_id=call.message.chat.id, text=girl_text_cats[-1], reply_markup=markup)

    for k in male:
        if call.data == k:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            bot.send_photo(call.message.chat.id, photo=open(f'''./boy/{k}''', 'rb'))
            markup = types.InlineKeyboardMarkup(row_width=1)

            if male.index(k) + 1 > len(male) - 1:
                btn9 = types.InlineKeyboardButton("📝Купить", callback_data='buy')
                btn10 = types.InlineKeyboardButton("◀️Назад", callback_data=male[male.index(k) - 1])
                btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page_kittens')
                markup.add(btn9,btn10, btn8)

            elif male.index(k) == 0:
                btn7 = types.InlineKeyboardButton("▶️Далее", callback_data=male[male.index(k) + 1])
                btn9 = types.InlineKeyboardButton("📝Купить", callback_data='buy')
                btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page_kittens')
                markup.add(btn7, btn9, btn8)
                bot.send_message(chat_id=call.message.chat.id, text=boy_text_cats[0], reply_markup=markup)
                bot.delete_message(call.message.chat.id, call.message.message_id)

            else:
                btn7 = types.InlineKeyboardButton("▶️Далее", callback_data=male[male.index(k) + 1])
                btn10 = types.InlineKeyboardButton("◀️Назад", callback_data=male[male.index(k) - 1])
                btn9 = types.InlineKeyboardButton("📝Купить", callback_data='buy')
                btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page_kittens')
                markup.add(btn9, btn7, btn10,btn8)
                bot.send_message(chat_id=call.message.chat.id, text=boy_text_cats[1], reply_markup=markup)
                bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(chat_id=call.message.chat.id, text=boy_text_cats[-1], reply_markup=markup)

    if call.data == "ru":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("😻Питомцы в наличии", callback_data='main')
        btn2 = types.InlineKeyboardButton("📌Информация о нас", callback_data='info')
        markup.add(btn1, btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="<b> ✋Вас приветствует питомник британских золотых шиншилл Amore Mia. </b> \n"
                                   "😸У нас вы можете приобрести котят как в домашние любимцы так и в разведение .\n"
                                   "🚌Доставка котят по всему миру .\n"
                                   "📎Доступные контакты ,социальные сети ,вы найдете в пункте <b> «Информация о нас».</b>",
                              reply_markup=markup, parse_mode='html')

    if call.data == "info":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("📱Вконтакте", url="https://vk.com/id172609070")
        btn2 = types.InlineKeyboardButton("📱Инстаграм", url="https://www.instagram.com/amore_mia_cattery")
        btn3 = types.InlineKeyboardButton("📱Телеграмм", url="https://t.me/Amore_mia32")
        # btn4 = types.InlineKeyboardButton("📞Контактный номер заводчика", callback_data='number')
        btn5 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.add(btn1,btn3,btn2,btn5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text="<b> Информация о нас: </b>", reply_markup=markup,parse_mode='html')

    elif call.data == "back_info":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("📱Вконтакте", url="https://vk.com/id172609070")
        btn4 = types.InlineKeyboardButton("📱Инстаграм", url="https://www.instagram.com/amore_mia_cattery")
        btn3 = types.InlineKeyboardButton("📱Телеграмм", url="https://t.me/Amore_mia32")
        btn2 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.add(btn1, btn4, btn3, btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="<b> Информация о нас: </b>", reply_markup=markup, parse_mode='html')

    elif call.data == 'main':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn4 = types.InlineKeyboardButton(f'🐱Девочка ({len(females)})', callback_data="girl")
        btn5 = types.InlineKeyboardButton(f'😸Мальчик ({len(male)})', callback_data="boy")
        markup.row(btn4, btn5)
        btn6 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.row(btn6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="Выберите пол питомца:", reply_markup=markup)

    elif call.data == 'girl':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id, photo=open(f'''./girl/{females[0]}''', 'rb'))
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn7 = types.InlineKeyboardButton("▶️Далее", callback_data=females[1])
        btn9 = types.InlineKeyboardButton("📝Купить", callback_data='buy')
        btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page_kittens')
        markup.add(btn7, btn9, btn8)
        bot.send_message(chat_id=call.message.chat.id, text=girl_text_cats[0], reply_markup=markup)

    elif call.data == 'boy':
        bot.send_photo(call.message.chat.id, photo=open(f'''./boy/{male[0]}''', 'rb'))
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn7 = types.InlineKeyboardButton("▶️Далее", callback_data=male[1])
        btn9 = types.InlineKeyboardButton("📝Купить", callback_data='buy')
        btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page_kittens')
        markup.add(btn7,btn8, btn9)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text=boy_text_cats[0], reply_markup=markup)

    elif call.data == "back_to_main_page_kittens":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton("😻Питомцы в наличии", callback_data='main')
        btn3 = types.InlineKeyboardButton("📌Информация о нас", callback_data='info')
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        markup.add(btn2, btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="<b> ✋Вас приветствует питомник британских золотых шиншилл Amore Mia. </b> \n"
                                   "😸У нас вы можете приобрести котят как в домашние любимцы так и в разведение"
                                   "🚌Доставка котят по всему миру .\n"
                                   "📎Доступные контакты ,социальные сети ,вы найдете в пункте  «информация о нас».",
                              reply_markup=markup, parse_mode='html')


    elif call.data == "back_to_main_page":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton("😻Питомцы в наличии", callback_data='main')
        btn3 = types.InlineKeyboardButton("📌Информация о нас", callback_data='info')
        markup.add(btn2, btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,

                              text="<b> ✋Вас приветствует питомник британских золотых шиншилл Amore Mia. </b> \n"
                                   "😸У нас вы можете приобрести котят как в домашние любимцы так и в разведение"
                                   "🚌Доставка котят по всему миру .\n"
                                   "📎Доступные контакты ,социальные сети ,вы найдете в пункте  «информация о нас».",
                              reply_markup=markup, parse_mode='html')

    if call.data == "en":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("😻Pets available", callback_data='main_en')
        btn2 = types.InlineKeyboardButton("📌Information about us", callback_data='info_en')
        markup.add(btn1, btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="<b> ✋Welcome to British golden chinchilla cattery Amore Mia. </b> \n"
                                   "😸Here you can buy kittens as pets and for breeding .\n"
                                   "🚌Delivery of kittens worldwide .\n"
                                   "📎Available contacts, social networks, you will find in the paragraph "
                                   "'<b> Information about us'</b>.",
                              reply_markup=markup, parse_mode='html')

    elif call.data == "info_en":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("📱Breeder's instagram", url="https://www.instagram.com/amore_mia_cattery")
        # btn2 = types.InlineKeyboardButton("📞Breeder's contact number", callback_data='number_en')
        btn3 = types.InlineKeyboardButton("📱telegrams", url="https://t.me/Amore_mia32")
        btn4 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page_en')
        markup.add(btn1,btn3, btn4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="<b> Information about us: </b>", reply_markup=markup, parse_mode='html')

    elif call.data == "number_en":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page_en')
        btn2 = types.InlineKeyboardButton("◀️back", callback_data='back_info_en')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="Available social networks by number - Telegram, \n"
                                  "                 8-953-286-39-26", reply_markup=markup)

    elif call.data == "back_info_en":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("📱Breeder's instagram", url="https://www.instagram.com/amore_mia_cattery")
        btn2 = types.InlineKeyboardButton("📞Breeder's contact number", callback_data='number_en')
        btn3 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page_en')
        markup.add(btn1, btn2, btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="<b> Information about us: </b>", reply_markup=markup, parse_mode='html')

    elif call.data == 'main_en':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(f'🐱females ({len(females)})', callback_data="girl_en")
        btn2 = types.InlineKeyboardButton(f'😸male ({len(male)})', callback_data="boy_en")
        markup.row(btn1, btn2)
        btn6 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page_en')
        markup.row(btn6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="Select your pet's gender:", reply_markup=markup)

    elif call.data == 'girl_en':
        bot.send_photo(call.message.chat.id, photo=open(f'''./girl_en/{females_en[0]}''', 'rb'))
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("▶️Further", callback_data=females_en[1])
        btn2 = types.InlineKeyboardButton("📝buy", callback_data='buy_en')
        btn3 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page_cats_en')
        markup.add(btn2, btn1,btn3)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text=girl_text_cats[0], reply_markup=markup)

    elif call.data == 'boy_en':
        bot.send_photo(call.message.chat.id, photo=open(f'''./boy_en/{male_en[0]}''', 'rb'))
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("▶️Further", callback_data=male_en[1])
        btn2 = types.InlineKeyboardButton("📝buy", callback_data='buy_en')
        btn3 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page_cats_en')
        markup.add(btn2, btn1, btn3)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text=boy_text_cats[0], reply_markup=markup)

    elif call.data == 'back_to_main_page_cats_en':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("😻Pets available", callback_data='main_en')
        btn2 = types.InlineKeyboardButton("📌Information about us", callback_data='info_en')
        bot.delete_message(call.message.chat.id, call.message.message_id-1)
        markup.add(btn1, btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="<b> ✋Welcome to British golden chinchilla cattery Amore Mia. </b> \n"
                                   "😸Here you can buy kittens as pets and for breeding .\n"
                                   "🚌Delivery of kittens worldwide .\n"
                                   "📎Available contacts, social networks, you will find in the paragraph 'information "
                                   "about us'.",
                              reply_markup=markup, parse_mode='html')

    elif call.data == 'back_to_main_page_en':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("😻Pets available", callback_data='main_en')
        btn2 = types.InlineKeyboardButton("📌Information about us", callback_data='info_en')
        markup.add(btn1, btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="<b> ✋Welcome to British golden chinchilla cattery Amore Mia. </b> \n"
                                   "😸Here you can buy kittens as pets and for breeding .\n"
                                   "🚌Delivery of kittens worldwide .\n"
                                   "📎Available contacts, social networks, you will find in the paragraph 'information "
                                   "about us'.",
                              reply_markup=markup, parse_mode='html')


bot.polling(none_stop=True)
