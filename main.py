import telebot
from telebot import types
from time import sleep
import os

picture = open('./data/2.jpg', 'rb')
picture2 = open('./data/3.jpg','rb')
picture3 = open('./mail/1.jpg','rb')
picture4 = open('./mail/2.jpg','rb')
picture5 = open('./mail/3.jpg', 'rb')
token = "6474703393:AAE8JBaernftP0-SElrKPQU8wOyadjT49v0"
bot = telebot.TeleBot(token)
img = open('./data/1.jpg', 'rb')


@bot.message_handler(commands=['start'])
def start_handler(message):
    print('test commit')
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn2 = types.InlineKeyboardButton("😻Питомцы в наличии",callback_data='main')
    btn3 = types.InlineKeyboardButton("📌Информация о нас", callback_data='info')
    markup.add(btn2, btn3)
    bot.send_message(message.chat.id, '<b> Приветствуем Вас в питомнике Amore-Mia </b> 😽 \n'
                                      '<b> Выберите соответствующую ячейку </b>', reply_markup=markup, parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "info":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("📱Связь с заводчиком", url="https://vk.com/id172609070")
        btn2 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        btn3 = types.InlineKeyboardButton("📞Контактный номер заводчика", callback_data='number')
        markup.add(btn1,btn2,btn3)
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
        btn1 = types.InlineKeyboardButton("📱Связь с заводчиком", url="https://vk.com/id172609070")
        btn2 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        btn3 = types.InlineKeyboardButton("📞Контактный номер заводчика", callback_data='number')
        markup.add(btn1, btn2, btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="<b> Информация о нас: </b>", reply_markup=markup,parse_mode='html')

    elif call.data == 'main':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn4 = types.InlineKeyboardButton("🐱Female", callback_data = "cotgirl")
        btn5 = types.InlineKeyboardButton("😸Male", callback_data = "cotman")
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
        btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.add(btn7, btn8)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
        bot.send_message(chat_id=call.message.chat.id, text="Нажмите 'далее' для фото следующего котёнка",reply_markup=markup)

    elif call.data == 'cotman':
        bot.send_photo(call.message.chat.id, photo=open('./mail/1.jpg', 'rb'), caption="Amore Mia Eaton ny1133(1233),\n"
                                                                                       "07.06.23,\n"
                                                                                       "F. ny1233,\n"
                                                                                       "M. by1133(1233)")
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn7 = types.InlineKeyboardButton("Далее", callback_data="next2")
        btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.add(btn7, btn8)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
        bot.send_message(chat_id=call.message.chat.id, text="Нажмите 'далее' для фото следующего котёнка",
                         reply_markup=markup)

    elif call.data == 'next':
        bot.send_photo(call.message.chat.id, photo=open('./data/3.jpg', 'rb'), caption="Amore Mia Frida ny12,\n"
                                                                                       "08.06.23,\n"
                                                                                       "F.BLN ny12,\n"
                                                                                       "M. ny25")
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn10 = types.InlineKeyboardButton("◀️Назад", callback_data='back')
        markup.add(btn10)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
        bot.send_message(chat_id=call.message.chat.id, text="Для того чтобы посмотреть мальчиков (Mail),\n"
                         "Нажмите '◀️Назад' ", reply_markup = markup)

    elif call.data == 'next2':
        bot.send_photo(call.message.chat.id, photo=open('./mail/2.jpg', 'rb'), caption="Amore Mia Elwin ny1133(1233),\n"
                                                                                       "07.06.23,\n"
                                                                                       "F. ny1233,\n"
                                                                                       "M. by1133(1233)")
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn7 = types.InlineKeyboardButton("Далее", callback_data="next3")
        btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.add(btn7, btn8)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
        bot.send_message(chat_id=call.message.chat.id, text="Нажмите 'далее' для фото следующего котёнка",
                         reply_markup=markup)

    elif call.data == 'next3':
        bot.send_photo(call.message.chat.id, photo=open('./mail/3.jpg', 'rb'), caption="Amore Mia Edwin my 1133(1233),\n"
                                                                                       "07.06.23,\n"
                                                                                       "F. ny1233,\n"
                                                                                       "M. by1133(1233)")
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn10 = types.InlineKeyboardButton("◀️Назад", callback_data='back')
        btn8 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.add(btn8, btn10)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
        bot.send_message(chat_id=call.message.chat.id, text="Нажмите '◀️В главное меню' если хотите вернуться в основное окошко, \n"
                                                            "Если хотите увидеть девочек (Female).Нажмите'◀️Назад' ",
                         reply_markup=markup)

    elif call.data == 'back':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn4 = types.InlineKeyboardButton("🐱Female", callback_data="cotgirl")
        btn5 = types.InlineKeyboardButton("😸Male", callback_data="cotman")
        markup.row(btn4, btn5)
        btn6 = types.InlineKeyboardButton("◀️В главное меню", callback_data='back_to_main_page')
        markup.row(btn6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите пол питомца:", reply_markup=markup)

    elif call.data == 'back_to_main_page':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton("😻Питомцы в наличии", callback_data='main')
        btn3 = types.InlineKeyboardButton("📌Информация о нас", callback_data='info')
        markup.add(btn2, btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='<b> Приветствуем Вас в питомнике Amore-Mia </b> 😽 \n'
                                           '<b> Выберите соответствующую ячейку </b>', reply_markup=markup,
                           parse_mode='html')


bot.polling(none_stop=True)
