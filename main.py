import telebot
import os
from telebot import types


token = "6474703393:AAE8JBaernftP0-SElrKPQU8wOyadjT49v0"
bot = telebot.TeleBot(token)


females = os.listdir('./girl')
male = os.listdir('./boy')

females_en = os.listdir('./girl')
male_en = os.listdir('./boy')




@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Русский",callback_data='ru')
    btn2 = types.InlineKeyboardButton("English", callback_data='en')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, '<b> 😽Пожалуйста,выберите язык. </b>  \n'
                                      '<b> Please select a language.😽 </b>', reply_markup=markup, parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global females, male
    for i in females:
        if call.data == i:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            bot.send_photo(call.message.chat.id, photo=open(f'''./girl/{i}''', 'rb'))
            markup = types.InlineKeyboardMarkup(row_width=1)

            if females.index(i) + 1 > len(females) - 1:
                btn9 = types.InlineKeyboardButton("Забронировать", callback_data='book')
                btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page33')
                markup.add(btn9, btn8)
            else:
                btn7 = types.InlineKeyboardButton("Далее", callback_data=females[females.index(i) + 1])
                btn9 = types.InlineKeyboardButton("Забронировать", callback_data='book')
                btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page33')
                markup.add(btn7, btn9, btn8)

            bot.send_message(chat_id=call.message.chat.id, text="Amore Mia Frida ny12 \n"
                                                                " 08.06.23 \n"
                         "F.BLN ny12 \n"
                         "M. ny25", reply_markup=markup)

    for i in male:
        if call.data == i:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            bot.send_photo(call.message.chat.id, photo=open(f'''./boy/{i}''', 'rb'))
            markup = types.InlineKeyboardMarkup(row_width=1)

            if male.index(i) + 1 > len(male) - 1:
                btn9 = types.InlineKeyboardButton("Забронировать", callback_data='book')
                btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page33')
                markup.add(btn9, btn8)
            else:
                btn7 = types.InlineKeyboardButton("Далее", callback_data=male[male.index(i) + 1])
                btn9 = types.InlineKeyboardButton("Забронировать", callback_data='book')
                btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page33')
                markup.add(btn7, btn9, btn8)

            bot.send_message(chat_id=call.message.chat.id, text="Amore Mia Elwin ny1133(1233) \n"
                                                                "08.06.23 \n"
                                                                "F.BLN ny12 \n"
                                                                "M. ny25", reply_markup=markup)

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
        btn7 = types.InlineKeyboardButton("Далее", callback_data=females[1])
        btn9 = types.InlineKeyboardButton("Забронировать", callback_data='book')
        btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page33')
        markup.add(btn7, btn9, btn8)

        bot.send_message(chat_id=call.message.chat.id, text="Amore Mia ny12,"
                                                            " 08.06.23       \n"
                     "F.BLN ny12 \n"
                     "M. ny25", reply_markup=markup)

    elif call.data == 'boy':
        bot.send_photo(call.message.chat.id, photo=open(f'''./boy/{male[0]}''', 'rb'))
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn7 = types.InlineKeyboardButton("Далее", callback_data=male[1])
        btn9 = types.InlineKeyboardButton("Забронировать", callback_data='book')
        btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page33')
        markup.add(btn7,btn8, btn9)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Amore Mia Eaton ny1133(1233)\n"
                         "07.06.23 \n"
                         "F. ny1233,\n"
                         "M. by1133(1233)", reply_markup=markup)

    elif call.data == "back_to_main_page_сats":
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

     females_en = os.listdir('./girl')
    # доделат for i in females_en:
        if call.data == i:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            bot.send_photo(call.message.chat.id, photo=open(f'''./girl/{i}''', 'rb'))
            markup = types.InlineKeyboardMarkup(row_width=1)

            if females_en.index(i) + 1 > len(females_en) - 1:
                btn9 = types.InlineKeyboardButton("book", callback_data='book')
                btn8 = types.InlineKeyboardButton("◀️️To main menu", callback_data='back_to_main_page_en')
                markup.add(btn9, btn8)
            else:
                btn7 = types.InlineKeyboardButton("Further", callback_data=females_en[females_en.index(i) + 1])
                btn9 = types.InlineKeyboardButton("book", callback_data='book')
                btn8 = types.InlineKeyboardButton("◀️️To main menu", callback_data='back_to_main_page_en')
                markup.add(btn7, btn9, btn8)

            bot.send_message(chat_id=call.message.chat.id, text="Amore Mia Frida ny12 \n"
                                                                " 08.06.23 \n"
                                                                "F.BLN ny12 \n"
                                                                "M. ny25", reply_markup=markup)
# доделать
    for i in male:
        male_en = os.listdir('./boy')
        if call.data == i:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            bot.send_photo(call.message.chat.id, photo=open(f'''./boy/{i}''', 'rb'))
            markup = types.InlineKeyboardMarkup(row_width=1)

            if male.index(i) + 1 > len(male) - 1:
                btn9 = types.InlineKeyboardButton("Забронировать", callback_data='book')
                btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page33')
                markup.add(btn9, btn8)
            else:
                btn7 = types.InlineKeyboardButton("Далее", callback_data=male_en[male_en.index(i) + 1])
                btn9 = types.InlineKeyboardButton("Забронировать", callback_data='book')
                btn8 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page33')
                markup.add(btn7, btn9, btn8)

            bot.send_message(chat_id=call.message.chat.id, text="Amore Mia Elwin ny1133(1233) \n"
                                                                "08.06.23 \n"
                                                                "F.BLN ny12 \n"
                                                                "M. ny25", reply_markup=markup)

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
        bot.send_photo(call.message.chat.id, photo=open(f'''./girl/{females_en[0]}''', 'rb'))
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("Further", callback_data=females_en[1])
        btn2 = types.InlineKeyboardButton("book", callback_data='book_en')
        btn3 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page_cats_en')
        markup.row(btn1, btn2,btn3)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
        bot.send_message(chat_id=call.message.chat.id, text="Amore Mia ny12,\n"
                                                            "08.06.23 \n"
                                                            "F.BLN ny12 \n"
                                                            "M. ny25", reply_markup=markup)

    elif call.data == 'boy_en':
        bot.send_photo(call.message.chat.id, photo=open(f'''./boy/{male[0]}''', 'rb'))
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("Further", callback_data=male[1])
        btn2 = types.InlineKeyboardButton("book", callback_data='book1')
        btn3 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page_cats_en')
        markup.row(btn1, btn2, btn3)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
        bot.send_message(chat_id=call.message.chat.id, text="Amore Mia Eaton ny1133(1233)\n"
                                                            "07.06.23 \n"
                                                            "F. ny1233,\n"
                                                            "M. by1133(1233)", reply_markup=markup)

    elif call.data == 'back_to_main_page_cats_en':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("😻Pets available", callback_data='main1')
        btn2 = types.InlineKeyboardButton("📌Information about us", callback_data='info1')
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
        btn1 = types.InlineKeyboardButton("😻Pets available", callback_data='main1')
        btn2 = types.InlineKeyboardButton("📌Information about us", callback_data='info1')
        markup.add(btn1, btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="<b> ✋Welcome to British golden chinchilla cattery Amore Mia. </b> \n"
                                   "😸Here you can buy kittens as pets and for breeding .\n"
                                   "🚌Delivery of kittens worldwide .\n"
                                   "📎Available contacts, social networks, you will find in the paragraph 'information "
                                   "about us'.",
                              reply_markup=markup, parse_mode='html')


bot.polling(none_stop=True)