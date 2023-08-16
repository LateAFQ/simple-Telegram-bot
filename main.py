import telebot
from telebot import types

token = "6474703393:AAE8JBaernftP0-SElrKPQU8wOyadjT49v0"
bot = telebot.TeleBot(token)

picture = open('./data/2.jpg', 'rb')
picture2 = open('./data/3.jpg','rb')
picture3 = open('./mail/1.jpg','rb')
picture4 = open('./mail/2.jpg','rb')
picture5 = open('./mail/3.jpg', 'rb')
img = open('./data/1.jpg', 'rb')


# TODO: Под фото котят, добавь кнопку "Забронировать"
# TODO: Сделай так, чтобы при нажатии на кнопки, удалялась предыдущая информация (Это делать последним)
@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Русский",callback_data='Ru')
    btn2 = types.InlineKeyboardButton("English", callback_data='En')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, '<b> 😽Пожалуйста,выберите язык. </b>  \n'
                                      '<b> Please select a language.😽 </b>', reply_markup=markup, parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # TODO: call.data === ru, зачем с верхний регистр?
    if call.data == "Ru":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("😻Питомцы в наличии", callback_data='main')
        btn2 = types.InlineKeyboardButton("📌Информация о нас", callback_data='info')
        markup.add(btn1, btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="<b> ✋Вас приветствует питомник британских золотых шиншилл Amore Mia. </b> \n"
                                   "😸У нас вы можете приобрести котят как в домашние любимцы так и в разведение .\n"
                                   "🚌Доставка котят по всему миру .\n"
                                   "📎Доступные контакты ,социальные сети ,вы найдете в пункте  «информация о нас».",
                              reply_markup=markup, parse_mode='html')

    if call.data == "info":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("📱Вконтакте", url="https://vk.com/id172609070")
        btn2 = types.InlineKeyboardButton("📱Инстаграм", url="https://www.instagram.com/amore_mia_cattery")
        btn3 = types.InlineKeyboardButton("📱Телеграмм", url="https://vk.com/id172609070")
        btn4 = types.InlineKeyboardButton("📞Контактный номер заводчика", callback_data='number')
        btn5 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.add(btn1,btn2,btn5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text="<b> Информация о нас: </b>", reply_markup=markup,parse_mode='html')

    elif call.data == "number":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        btn10 = types.InlineKeyboardButton("◀️Назад", callback_data='back_info')
        markup.add(btn2,btn10)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="Доступные соц-сети по номеру - Telegram, \n"
                                 "                 8-953-286-39-26", reply_markup=markup)

    elif call.data == "back_info":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("📱Вконтакте", url="https://vk.com/id172609070")
        btn4 = types.InlineKeyboardButton("📱Инстаграм", url="https://www.instagram.com/amore_mia_cattery")
        btn3 = types.InlineKeyboardButton("📞Контактный номер заводчика", callback_data='number')
        btn2 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.add(btn1, btn4, btn3, btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="<b> Информация о нас: </b>", reply_markup=markup, parse_mode='html')

    elif call.data == 'main':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn4 = types.InlineKeyboardButton("🐱Девочка", callback_data="cotgirl")
        btn5 = types.InlineKeyboardButton("😸Мальчик", callback_data="cotman")
        markup.row(btn4, btn5)
        btn6 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.row(btn6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="Выберите пол питомца:", reply_markup=markup)

    elif call.data == 'cotgirl':
        bot.send_photo(call.message.chat.id, photo=open('./data/2.jpg', 'rb'), caption="Amore Mia ny12,\n"
                                                                                       "08.06.23,\n"
                                                                                       "F.BLN ny12,\n"
                                                                                       "M. ny25")
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn7 = types.InlineKeyboardButton("Далее", callback_data="next")
        btn9 = types.InlineKeyboardButton("Забронировать", callback_data='book')
        markup.row(btn7, btn9)
        btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.row(btn8)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
        bot.send_message(chat_id=call.message.chat.id,text = "test",reply_markup=markup)

    elif call.data == 'cotman':
        bot.send_photo(call.message.chat.id, photo=open('./mail/1.jpg', 'rb'), caption="Amore Mia Eaton ny1133(1233),\n"
                                                                                       "07.06.23,\n"
                                                                                       "F. ny1233,\n"
                                                                                       "M. by1133(1233)")
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn7 = types.InlineKeyboardButton("Далее", callback_data="next")
        btn9 = types.InlineKeyboardButton("Забронировать", callback_data='book')
        markup.row(btn7, btn9)
        btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.row(btn8)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
        bot.send_message(chat_id=call.message.chat.id,text="test",reply_markup=markup)

    elif call.data == 'next':
        bot.send_photo(call.message.chat.id, photo=open('./data/3.jpg', 'rb'), caption="Amore Mia Frida ny12,\n"
                                                                                       "08.06.23,\n"
                                                                                       "F.BLN ny12,\n"
                                                                                       "M. ny25")
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn10 = types.InlineKeyboardButton("◀️Назад", callback_data='back')
        btn9 = types.InlineKeyboardButton("Забронировать", callback_data='book')
        markup.row(btn10, btn9)
        btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.row(btn8)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
        bot.send_message(chat_id=call.message.chat.id,text="test",reply_markup = markup)

    elif call.data == 'next2':
        bot.send_photo(call.message.chat.id, photo=open('./mail/2.jpg', 'rb'), caption="Amore Mia Elwin ny1133(1233),\n"
                                                                                       "07.06.23,\n"
                                                                                       "F. ny1233,\n"
                                                                                       "M. by1133(1233)")

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn10 = types.InlineKeyboardButton("◀️Назад", callback_data='back')
        btn9 = types.InlineKeyboardButton("Забронировать", callback_data='book')
        markup.row(btn10, btn9)
        btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.row(btn8)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
        bot.send_message(chat_id=call.message.chat.id,text="test",reply_markup=markup)

    elif call.data == 'back':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn4 = types.InlineKeyboardButton("🐱Female", callback_data="cotgirl")
        btn5 = types.InlineKeyboardButton("😸Male", callback_data="cotman")
        markup.row(btn4, btn5)
        btn6 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.row(btn6)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="Выберите пол питомца:", reply_markup=markup)

    if call.data == "back_to_main_page":
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

    if call.data == "En":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("😻Pets available", callback_data='main1')
        btn2 = types.InlineKeyboardButton("📌Information about us", callback_data='info1')
        markup.add(btn1, btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="<b> ✋Welcome to British golden chinchilla cattery Amore Mia. </b> \n"
                                   "😸Here you can buy kittens as pets and for breeding .\n"
                                   "🚌Delivery of kittens worldwide .\n"
                                   "📎Available contacts, social networks, you will find in the paragraph "
                                   "'information about us'.",
                              reply_markup=markup, parse_mode='html')

    elif call.data == "info1":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("📱Breeder's instagram", url="https://www.instagram.com/amore_mia_cattery")
        btn2 = types.InlineKeyboardButton("📞Breeder's contact number", callback_data='number1')
        btn3 = types.InlineKeyboardButton("📱telegrams", url="https://vk.com/id172609070")
        btn4 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page1')
        markup.add(btn1, btn4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="<b> Information about us: </b>", reply_markup=markup, parse_mode='html')

    elif call.data == "number1":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page1')
        btn2 = types.InlineKeyboardButton("◀️back", callback_data='back_info1')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="Available social networks by number - Telegram, \n"
                                  "                 8-953-286-39-26", reply_markup=markup)

    elif call.data == "back_info1":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("📱Breeder's instagram", url="https://www.instagram.com/amore_mia_cattery")
        btn2 = types.InlineKeyboardButton("📞Breeder's contact number", callback_data='number1')
        btn3 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page1')
        markup.add(btn1, btn2, btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="<b> Information about us: </b>", reply_markup=markup, parse_mode='html')

    elif call.data == 'main1':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("🐱Female", callback_data="cotgirl1")
        btn2 = types.InlineKeyboardButton("😸Male", callback_data="cotman1")
        markup.row(btn1, btn2)
        btn6 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page1')
        markup.row(btn6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="Select your pet's gender:", reply_markup=markup)

    elif call.data == 'cotgirl1':
        bot.send_photo(call.message.chat.id, photo=open('./data/2.jpg', 'rb'), caption="Amore Mia ny12,\n"
                                                                                       "08.06.23,\n"
                                                                                       "F.BLN ny12,\n"
                                                                                       "M. ny25")
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("Further", callback_data="next1")
        btn2 = types.InlineKeyboardButton("book", callback_data='book1')
        markup.row(btn1, btn2)
        btn3 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page1')
        markup.row(btn3)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
        bot.send_message(chat_id=call.message.chat.id,text="test",reply_markup=markup)

    elif call.data == 'cotman1':
        bot.send_photo(call.message.chat.id, photo=open('./mail/1.jpg', 'rb'), caption="Amore Mia Eaton ny1133(1233),\n"
                                                                                       "07.06.23,\n"
                                                                                       "F. ny1233,\n"
                                                                                       "M. by1133(1233)")
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("Further", callback_data="next1")
        btn2 = types.InlineKeyboardButton("book", callback_data='book1')
        markup.row(btn1, btn2)
        btn3 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page1')
        markup.row(btn3)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
        bot.send_message(chat_id=call.message.chat.id, text="test", reply_markup=markup)

    elif call.data == 'next1':
        bot.send_photo(call.message.chat.id, photo=open('./data/3.jpg', 'rb'), caption="Amore Mia Frida ny12,\n"
                                                                                       "08.06.23,\n"
                                                                                       "F.BLN ny12,\n"
                                                                                       "M. ny25")
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton("book", callback_data='book1')
        btn3 = types.InlineKeyboardButton("◀️Back", callback_data='back1')
        markup.row(btn2,btn3)
        btn1 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page1')
        markup.row(btn1)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
        bot.send_message(chat_id=call.message.chat.id,text="test",reply_markup=markup)

    elif call.data == 'next3':
        bot.send_photo(call.message.chat.id, photo=open('./mail/2.jpg', 'rb'), caption="Amore Mia Elwin ny1133(1233)\n"
                                                                                       "07.06.23\n"
                                                                                       "F. ny1233\n"
                                                                                       "M. by1133(1233)")

        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton("book", callback_data='book1')
        btn3 = types.InlineKeyboardButton("◀️Back", callback_data='back1')
        markup.row(btn2, btn3)
        btn1 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page1')
        markup.row(btn1)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
        bot.send_message(chat_id=call.message.chat.id, text="test", reply_markup=markup)

    elif call.data == 'back1':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("🐱Female", callback_data="cotgirl1")
        btn2 = types.InlineKeyboardButton("😸Male", callback_data="cotman1")
        markup.row(btn1, btn2)
        btn6 = types.InlineKeyboardButton("◀️To main menu", callback_data='back_to_main_page1')
        markup.row(btn6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Select your pet's gender:", reply_markup=markup)

    elif call.data == 'back_to_main_page1':
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
