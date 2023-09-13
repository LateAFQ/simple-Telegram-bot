import telebot
import os
from telebot import types
import configparser
import sqlite3
import database

config = configparser.ConfigParser()
config.read('config.ini')
token = config['DEFAULT']['token']

bot = telebot.TeleBot(token)

# Про разделения русского и англиского я еще подумаю, как лучше сделать, может и такой вариант будет лучшим
try:
    females = os.listdir('./data/img/img_girl')
    male = os.listdir('./data/img/img_boy')
    females_en = os.listdir('./data/img/img_girl_en')
    male_en = os.listdir('./data/img/img_boy_en')

    male_txt = os.listdir('data/text/boy_text')
    females_txt = os.listdir('data/text/girl_text')
    male_txt_en = os.listdir('data/text/boy_text_en')
    females_txt_en = os.listdir('data/text/girl_text_en')
except:
    os.mkdir('./data')
    os.mkdir('./data/img')
    os.mkdir('./data/text')

    os.mkdir('./data/img/img_girl')
    os.mkdir('./data/img/img_boy')
    os.mkdir('./data/img/img_girl_en')
    os.mkdir('./data/img/img_boy_en')

    os.mkdir('data/text/boy_text')
    os.mkdir('data/text/girl_text')
    os.mkdir('data/text/boy_text_en')
    os.mkdir('data/text/girl_text_en')

    females = os.listdir('./data/img/img_girl')
    male = os.listdir('./data/img/img_boy')
    females_en = os.listdir('./data/img/img_girl_en')
    male_en = os.listdir('./data/img/img_boy_en')

    male_txt = os.listdir('data/text/boy_text')
    females_txt = os.listdir('data/text/girl_text')
    male_txt_en = os.listdir('data/text/boy_text_en')
    females_txt_en = os.listdir('data/text/girl_text_en')


@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Русский", callback_data='ru')
    btn2 = types.InlineKeyboardButton("English", callback_data='en')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, '<b> 😽Пожалуйста,выберите язык. </b>  \n'
                                      '<b> Please select a language.😽 </b>', reply_markup=markup, parse_mode='html')


# Все ситуации я посмтрю завтра более детально, думаю можно как-то будет вынести в отдельную переменную язык и разветвление сделать чуть меньше и проще
# просто код полностью дублируется, а можно же проверять переменную lang и смотреть если англиский, то тодно выводить если наш РУССКИЙ, то другие


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global male_en, females_en, male_txt, females_txt

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
        btn5 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.add(btn1, btn3, btn2, btn5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="<b> Информация о нас: </b>", reply_markup=markup, parse_mode='html')

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
        if len(females) == 0:
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
            markup.add(btn1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='К сожалению сейчас, котят нет в наличии', reply_markup=markup)
            return

        for txt in females_txt:
            if txt.split('.')[0] == females[0].split('.')[0]:
                with open(f'''data/text/girl_text/{txt}''') as k:
                    text = k.read()
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id, photo=open(f'''./data/img/img_girl/{females[0]}''', 'rb'))
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn7 = types.InlineKeyboardButton("▶️Далее", callback_data=females[1])
        btn9 = types.InlineKeyboardButton("📝Забронировать", callback_data='book')
        btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page_kittens')
        markup.add(btn7, btn9, btn8)
        bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=markup)

    elif call.data == 'boy':
        if len(male) == 0:
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
            markup.add(btn1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='К сожалению сейчас, котят нет в наличии', reply_markup=markup)
            return

        for txt in male_txt:
            if txt.split('.')[0] == male[0].split('.')[0]:
                with open(f'''data/text/boy_text/{txt}''') as k:
                    text = k.read()
                bot.send_photo(call.message.chat.id, photo=open(f'''./data/img/img_boy/{male[0]}''', 'rb'))
                markup = types.InlineKeyboardMarkup(row_width=1)
                btn7 = types.InlineKeyboardButton("▶️Далее", callback_data=male[1])
                btn9 = types.InlineKeyboardButton("📝Забронировать", callback_data='book')
                btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page_kittens')
                markup.add(btn7, btn9, btn8)
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=markup)

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

    elif call.data == "book":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("📞Контактый номер", callback_data="number")
        btn2 = types.InlineKeyboardButton("📱Телеграмм", url="https://t.me/Amore_mia32")
        btn3 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.add(btn2, btn1, btn3)
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Снова приветствуем!😺\n'
                                   '                            \n'
                                   'Цена на каждого котенка - индивидуальна .\n'
                                   'И согласуется напрeмую с покупателем!\n'
                                   '\n'
                                   'Бронь котенка осуществляется при взносе задатка \n'
                                   'Если вас заинтересовал котенок,пожалуйста, свяжитесь с нами:⬇️',
                              reply_markup=markup)

    elif call.data == "number":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="back_book")
        btn2 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.add(btn1, btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Наш номер(Ru):89532863926',
                              reply_markup=markup)

    elif call.data == 'back_book':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("📞Контактый номер", callback_data="number")
        btn2 = types.InlineKeyboardButton("📱Телеграмм", url="https://t.me/Amore_mia32")
        btn3 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.add(btn2, btn1, btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Снова приветствуем!😺\n'
                                   '                            \n'
                                   'Цена на каждого котенка - индивидуальна .\n'
                                   'И согласуется напрeмую с покупателем!\n'
                                   '                                \n'
                                   'Бронь котенка осуществляется при взносе задатка \n'
                                   'Если вас заинтересовал котенок,пожалуйста, свяжитесь с нами:⬇️',
                              reply_markup=markup)

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
        markup.add(btn1, btn3, btn4)
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
        if len(females_en) == 0:
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page_en')
            markup.add(btn1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Sorry, there are no kittens available at the moment.', reply_markup=markup)
            return

        for txt in females_txt_en:
            if txt.split('.')[0] == females_en[0].split('.')[0]:
                with open(f'''data/text/girl_text_en/{txt}''') as k:
                    text = k.read()
                bot.send_photo(call.message.chat.id, photo=open(f'''./data/img/img_girl_en/{females_en[0]}''', 'rb'))
                markup = types.InlineKeyboardMarkup(row_width=1)
                btn1 = types.InlineKeyboardButton("▶️Further", callback_data=females_en[1])
                btn2 = types.InlineKeyboardButton("📝book", callback_data='book_en')
                btn3 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page_cats_en')
                markup.add(btn1, btn2, btn3)
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=markup)

    elif call.data == 'boy_en':
        if len(male_en) == 0:
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page_en')
            markup.add(btn1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Sorry, there are no kittens available at the moment.', reply_markup=markup)
            return

        for txt in male_txt_en:
            if txt.split('.')[0] == male_en[0].split('.')[0]:
                with open(f'''data/text/boy_text_en/{txt}''') as k:
                    text = k.read()
                bot.send_photo(call.message.chat.id, photo=open(f'''./data/img/img_boy_en/{male_en[0]}''', 'rb'))
                markup = types.InlineKeyboardMarkup(row_width=1)
                btn1 = types.InlineKeyboardButton("▶️Further", callback_data=male_en[1])
                btn2 = types.InlineKeyboardButton("📝book", callback_data='book_en')
                btn3 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page_cats_en')
                markup.add(btn1, btn2, btn3)
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=markup)

    elif call.data == "book_en":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("📞Breeder's contact number", callback_data='number_en')
        btn2 = types.InlineKeyboardButton("📱telegrams", url="https://t.me/Amore_mia32")
        btn3 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page_en')
        markup.add(btn2, btn1, btn3)
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Welcome again!😺\n'
                                   '\n'
                                   'The price for each kitten is individual .\n'
                                   'And agreed directly with the buyer!\n'
                                   '\n'
                                   'Reservation of a kitten is carried out upon payment of a deposit \n'
                                   'If you are interested in a kitten, please contact us:⬇️',
                              reply_markup=markup)

    elif call.data == "number_en":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("back", callback_data="back_book_en")
        btn2 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page_en')
        markup.add(btn1, btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='our phone number(Ru):89532863926',
                              reply_markup=markup)

    elif call.data == "back_book_en":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("📞Breeder's contact number", callback_data='number_en')
        btn2 = types.InlineKeyboardButton("📱telegrams", url="https://t.me/Amore_mia32")
        btn3 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page_en')
        markup.add(btn2, btn1, btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Welcome again!😺\n'
                                   '\n'
                                   'The price for each kitten is individual .\n'
                                   'And agreed directly with the buyer!\n'
                                   '\n'
                                   'Reservation of a kitten is carried out upon payment of a deposit \n'
                                   'If you are interested in a kitten, please contact us:⬇️',
                              reply_markup=markup)

    elif call.data == 'back_to_main_page_cats_en':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("😻Pets available", callback_data='main_en')
        btn2 = types.InlineKeyboardButton("📌Information about us", callback_data='info_en')
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
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

    for further_females_en in females_en:
        if call.data == further_females_en:
            for txt in females_txt_en:
                if txt.split('.')[0] == further_females_en.split('.')[0]:
                    with open(f'''data/text/girl_text_en/{txt}''') as k:
                        text = k.read()
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    bot.delete_message(call.message.chat.id, call.message.message_id - 1)
                    bot.send_photo(call.message.chat.id,
                                   photo=open(f'''./data/img/img.girl_en/{further_females_en}''', 'rb'))
                    markup = types.InlineKeyboardMarkup(row_width=1)

                    if females_en.index(further_females_en) + 1 > len(females_en) - 1:
                        btn9 = types.InlineKeyboardButton("📝book", callback_data='book_en')
                        btn7 = types.InlineKeyboardButton("◀️back", callback_data=females_en[
                            females_en.index(further_females_en) - 1])
                        btn8 = types.InlineKeyboardButton("◀️️To main menu", callback_data='back_to_main_page_cats_en')
                        markup.add(btn7, btn9, btn8)
                        bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=markup)

                    elif females_en.index(further_females_en) == 0:
                        btn7 = types.InlineKeyboardButton("📝book", callback_data='book_en')
                        btn9 = types.InlineKeyboardButton("▶️Further", callback_data=females_en[
                            females_en.index(further_females_en) + 1])
                        btn8 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page_cats_en')
                        markup.add(btn9, btn7, btn8)
                        bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=markup)

                    else:
                        btn7 = types.InlineKeyboardButton("▶️Further", callback_data=females_en[
                            females_en.index(further_females_en) + 1])
                        btn9 = types.InlineKeyboardButton("📝book", callback_data='book_en')
                        btn10 = types.InlineKeyboardButton("◀️back", callback_data=females_en[
                            females_en.index(further_females_en) - 1])
                        markup.row(btn10, btn7)
                        btn8 = types.InlineKeyboardButton("◀️️To main menu", callback_data='back_to_main_page_cats_en')
                        markup.add(btn9, btn8)
                        bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=markup)

    for further_male_en in male_en:
        if call.data == further_male_en:
            for txt in male_txt_en:
                if txt.split('.')[0] == further_male_en.split('.')[0]:
                    with open(f'''data/text/boy_text_en/{txt}''') as k:
                        text = k.read()
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    bot.delete_message(call.message.chat.id, call.message.message_id - 1)
                    bot.send_photo(call.message.chat.id,
                                   photo=open(f'''./data/img/img_boy_en/{further_male_en}''', 'rb'))
                    markup = types.InlineKeyboardMarkup(row_width=1)

                    if male_en.index(further_male_en) + 1 > len(male_en) - 1:
                        btn9 = types.InlineKeyboardButton("📝book", callback_data='book_en')
                        btn7 = types.InlineKeyboardButton("◀️back",
                                                          callback_data=male_en[male_en.index(further_male_en) - 1])
                        btn8 = types.InlineKeyboardButton("◀️️To main menu", callback_data='back_to_main_page_cats_en')
                        markup.add(btn7, btn9, btn8)
                        bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=markup)

                    elif male_en.index(further_male_en) == 0:
                        btn7 = types.InlineKeyboardButton("📝book", callback_data='book_en')
                        btn9 = types.InlineKeyboardButton("▶️Further",
                                                          callback_data=male_en[male_en.index(further_male_en) + 1])
                        btn8 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page_cats_en')
                        markup.add(btn9, btn7, btn8)
                        bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=markup)

                    else:
                        btn10 = types.InlineKeyboardButton("📝book", callback_data='book_en')
                        btn8 = types.InlineKeyboardButton("◀️back",
                                                          callback_data=male_en[male_en.index(further_male_en) - 1])
                        btn7 = types.InlineKeyboardButton("▶️Further",
                                                          callback_data=male_en[male_en.index(further_male_en) + 1])
                        markup.row(btn8, btn7)
                        btn9 = types.InlineKeyboardButton("◀️️To main menu", callback_data='back_to_main_page_cats_en')
                        markup.add(btn10, btn9)
                        bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=markup)

    for further_females in females:
        if call.data == further_females:
            for txt in database.get_catgirl()[:]:
                text = txt[0:][1:5]
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.delete_message(call.message.chat.id, call.message.message_id - 1)
                bot.send_photo(call.message.chat.id, photo=open(f'''./data/img/img_girl/{further_females}''', 'rb'))
                markup = types.InlineKeyboardMarkup(row_width=1)

                if females.index(further_females) + 1 > len(females) - 1:
                    btn9 = types.InlineKeyboardButton("📝Забронировать", callback_data='book')
                    btn10 = types.InlineKeyboardButton("◀️Назад",
                                                       callback_data=females[females.index(further_females) - 1])
                    btn11 = types.InlineKeyboardButton("◀️В главное меню",
                                                       callback_data='back_to_main_page_kittens')
                    markup.add(btn10, btn9, btn11)
                    bot.send_message(chat_id=call.message.chat.id, text=text,reply_markup=markup)

                elif females.index(further_females) == 0:
                    btn7 = types.InlineKeyboardButton("▶️Далее",
                                                      callback_data=females[females.index(further_females) + 1])
                    btn9 = types.InlineKeyboardButton("📝Забронировать", callback_data='book')
                    btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page_kittens')
                    markup.add(btn7, btn9, btn8)
                    bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=markup)

                else:
                    btn10 = types.InlineKeyboardButton("◀️Назад",
                                                       callback_data=females[females.index(further_females) - 1])
                    btn7 = types.InlineKeyboardButton("▶️Далее",
                                                      callback_data=females[females.index(further_females) + 1])
                    markup.row(btn10, btn7)
                    btn9 = types.InlineKeyboardButton("📝Забронировать", callback_data='book')
                    btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page_kittens')
                    markup.add(btn9, btn8)
                    bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=markup)


    for further_male in male:
        if call.data == further_male:
            for txt in male_txt:
                if txt.split('.')[0] == further_male.split('.')[0]:
                    with open(f'''data/text/boy_text/{txt}''') as k:
                        text = k.read()
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    bot.delete_message(call.message.chat.id, call.message.message_id - 1)
                    bot.send_photo(call.message.chat.id, photo=open(f'''./data/img/img_boy/{further_male}''', 'rb'))
                    markup = types.InlineKeyboardMarkup(row_width=1)

                    if male.index(further_male) + 1 > len(male) - 1:
                        btn9 = types.InlineKeyboardButton("📝Забронировать", callback_data='book')
                        btn10 = types.InlineKeyboardButton("◀️Назад", callback_data=male[male.index(further_male) - 1])
                        btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page_kittens')
                        markup.add(btn10, btn9, btn8)
                        bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=markup)

                    elif male.index(further_male) == 0:
                        btn7 = types.InlineKeyboardButton("▶️Далее", callback_data=male[male.index(further_male) + 1])
                        btn9 = types.InlineKeyboardButton("📝Забронировать", callback_data='book')
                        btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page_kittens')
                        markup.add(btn7, btn9, btn8)
                        bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=markup)

                    else:
                        btn7 = types.InlineKeyboardButton("▶️Далее", callback_data=male[male.index(further_male) + 1])
                        btn10 = types.InlineKeyboardButton("◀️Назад", callback_data=male[male.index(further_male) - 1])
                        markup.row(btn10, btn7)
                        btn9 = types.InlineKeyboardButton("📝Забронировать", callback_data='book')
                        btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page_kittens')
                        markup.add(btn9, btn8)
                        bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=markup)

bot.polling(none_stop=True)
