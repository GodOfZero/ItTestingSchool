import sqlite3
from sqlite3 import connect
import telebot
from telebot import types

bot = telebot.TeleBot('6105992511:AAHHw1UQ39NcZU0EewnCY8ZM-UtSmS5k5XE')
admin_id = 819119213
ldata = '9 серпня о 19:00'  # ldata='9 серпня о 19:00' не работает


@bot.message_handler(commands=['start'])
def start(message):
    # with open('chatids.txt','a+') as chatids:
    #     print(message.chat.id,file=chatids)
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS login_id( id INTEGER)")
    connect.commit()

    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")

    data = cursor.fetchone()
    if data is None:
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
        connect.commit()

    with open('chatids.txt', "r+") as user_file:
        if str(message.from_user.id) not in user_file.read().split("\n"):
            user_file.write(f'{message.from_user.id}\n')
    markup = types.InlineKeyboardMarkup()
    #btn1 = types.InlineKeyboardButton(text="Наш ТГ канал", url="https://t.me/freeittestingschool")
    btn2 = types.InlineKeyboardButton(text="Наш сайт", url="https://it-testing-school.com/ua")
    btn3 = types.InlineKeyboardButton(text="Контакти", url="https://it-testing-school.com/ua/contact-us")
    btn4 = types.InlineKeyboardButton(text="Оплата курсу", url="https://it-testing-school.com/ua/pay-for-qamanual")
    markup.add(btn2, btn3)
    markup.add(btn4)

    video = open('Photo/v1s.mp4', 'rb')
    bot.send_video(message.chat.id, video,
                   caption='Привіт👋🏼! \nВже зовсім скоро ми проведемо безкоштовне онлайн заняття з тестування ПЗ! \n\nКОЛИ? \n🗓 <b> 9 серпня о 19:00 </b> \n\nДЕ? \n🔗 Посилання на заняття буде у цій групі 📍 ближче до старту вебінару \n\nЦІЛЬ \n👨🏻‍💻 Дізнатися все про те, хто такий тестувальник та, що йому потрібно знати \n\nМи в Інстаграм:\nhttps://www.instagram.com/it_testing_school \n\nВиникли запитання?\n📞 +380 (99) 001 50 55\n💌 Або пишіть у Телеграм: @InnaTestingSchool',
                   reply_markup=markup)


@bot.message_handler(commands=['rassylka30'])
def rassylka(message):
    if message.chat.id == admin_id:
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("SELECT id FROM login_id")
        user_ids = cursor.fetchall()
        for user_id in user_ids:
            file = open('Photo/v30.mp4', 'rb')
            markup2 = types.InlineKeyboardMarkup()
            btn6 = types.InlineKeyboardButton(text="Посилання на безкоштовне заняття",
                                              url="https://us02web.zoom.us/j/81419393460")
            btn1 = types.InlineKeyboardButton(text="Наш ТГ канал", url="https://t.me/freeittestingschool")
            markup2.add(btn6)
            markup2.add(btn1)
            try:
                bot.send_video(user_id, file,
                               caption='❗️ Майже 30 хвилин до прямого ефіру.\nДе ми розповімо: \n \n😮 Як без досвіду в ІТ отримати роботу\n😮 Незалежно вам 15 чи 50 років\n😮 Працювати віддалено з дому\n😮 Як стабільно заробляти 1000$\n\n❌ Цю інформацію ніхто не розкаже!\n\n❗️ Через 30 хвилин ми розпочинаємо!',
                               reply_markup=markup2)
            except telebot.apihelper.ApiException:
                pass


@bot.message_handler(commands=['rassylka60'])
def rassylka(message):
    if message.chat.id == admin_id:
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("SELECT id FROM login_id")
        user_ids = cursor.fetchall()
        for user_id in user_ids:
            markup2 = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="Наш ТГ канал", url="https://t.me/freeittestingschool")
            markup2.add(btn1)
            file = open('Photo/v60.mp4', 'rb')
            try:
                bot.send_video(user_id, file, caption='1 година до початку!!!!!! 👀👀👀👀👀👀', reply_markup=markup2)
            except telebot.apihelper.ApiException:
                pass


@bot.message_handler(commands=['rassylka5'])
def rassylka(message):
    if message.chat.id == admin_id:
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("SELECT id FROM login_id")
        user_ids = cursor.fetchall()
        for user_id in user_ids:
            file = open('Photo/v5.mp4', 'rb')
            markup2 = types.InlineKeyboardMarkup()
            btn6 = types.InlineKeyboardButton(text="Посилання на безкоштовне заняття",
                                              url="https://us02web.zoom.us/j/81419393460")
            markup2.add(btn6)
            try:
                bot.send_video(user_id, file,
                               caption='🔊🔊🔊Хутчіше підключайся! 🔊🔊🔊\n\nПосилання на заняття: 👇🏼👇🏼👇🏼👇🏼👇🏼👇🏼',
                               reply_markup=markup2)
            except telebot.apihelper.ApiException:
                pass


@bot.message_handler(commands=['rassylka'])
def rassylka(message):
    if message.chat.id == admin_id:
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("SELECT id FROM login_id")
        user_ids = cursor.fetchall()
        for user_id in user_ids:
            file = open('Photo/vrassylka.mp4', 'rb')
            markup2 = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="Наш ТГ канал", url="https://t.me/freeittestingschool")
            markup2.add(btn1)
            try:
                bot.send_video(user_id, file,
                               caption='<b>Сьогодні о 19:00</b> в онлайні розкажемо:\n🔹 як можна заробляти з дому маючи ПК та інтернет\n🔹 як отримати високоплачувану віддалену професію\n🔹 як працевлаштуватись без досвіду\n🔹 як отримати 1000$ на міс.',
                               parse_mode='html', reply_markup=markup2)
            except telebot.apihelper.ApiException:
                pass


@bot.message_handler(commands=['rassylka120'])
def rassylka(message):
    if message.chat.id == admin_id:
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("SELECT id FROM login_id")
        user_ids = cursor.fetchall()
        for user_id in user_ids:
            file = open('Photo/v120.mp4', 'rb')
            markup2 = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="Наш ТГ канал", url="https://t.me/freeittestingschool")
            markup2.add(btn1)
            try:
                bot.send_video(user_id, file,
                               caption='<b>Через 2 години відбудеться захоплююче заняття з тестування ПЗ 🥳🥳🥳</b> \n\n<i>Підготуйтеся до нових викликів та поглиблення знань 😉</i>',
                               reply_markup=markup2, parse_mode='html')
            except telebot.apihelper.ApiException:
                pass


@bot.message_handler(commands=['rassylkastart'])
def rassylka(message):
    if message.chat.id == admin_id:
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("SELECT id FROM login_id")
        user_ids = cursor.fetchall()
        for user_id in user_ids:
            file = open('Photo/vstart.mp4', 'rb')
            markup2 = types.InlineKeyboardMarkup()
            btn6 = types.InlineKeyboardButton(text="Посилання на безкоштовне заняття",
                                              url="https://us02web.zoom.us/j/81419393460")
            markup2.add(btn6)
            try:
                bot.send_video(user_id, file,
                               caption='🔊🔊🔊 Хутчіше підключайся! 🔊🔊🔊\n\nПосилання на заняття: 👇🏼👇🏼👇🏼👇🏼👇🏼👇🏼',
                               reply_markup=markup2)
            except telebot.apihelper.ApiException:
                pass


@bot.message_handler(commands=['rassylkapromo'])
def rassylka(message):
    if message.chat.id == admin_id:
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("SELECT id FROM login_id")
        user_ids = cursor.fetchall()
        for user_id in user_ids:
            file = open('Photo/vpromo.mp4', 'rb')
            markup2 = types.InlineKeyboardMarkup()
            btn6 = types.InlineKeyboardButton(text="Посилання на безкоштовне заняття",
                                              url="https://us02web.zoom.us/j/81419393460")
            btn2 = types.InlineKeyboardButton(text="Наш сайт", url="https://it-testing-school.com/ua")
            markup2.add(btn6)
            markup2.add(btn2)
            try:
                bot.send_video(user_id, file, caption='Тільки сьогодні вас очікує <b>промокод на супер знижку</b> 🔥🔥🔥\nНе пропустіть!', reply_markup=markup2,
                               parse_mode='html')
            except telebot.apihelper.ApiException:
                pass


@bot.message_handler(commands=['rassylkaoplata'])
def rassylka(message):
    if message.chat.id == admin_id:
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("SELECT id FROM login_id")
        user_ids = cursor.fetchall()
        for user_id in user_ids:
            file = open('Photo/voplata.mp4', 'rb')
            markup2 = types.InlineKeyboardMarkup()
            btn6 = types.InlineKeyboardButton(text="Оплата курсу",
                                              url="https://it-testing-school.com/ua/pay-for-qamanual")
            markup2.add(btn6)
            try:
                bot.send_video(user_id, file, caption='<b>Ціна курсу зі знижкою 14600 грн.</b> \nТакож є оплата частинами\nДо 09.08 - 7300 грн\nДо 16.08 - 7300 грн\n\n🎁 <b>Сплатити курс можна за прямим посиланням: </b>👇🏼👇🏼👇🏼👇🏼👇🏼', reply_markup=markup2,
                               parse_mode='html')
            except telebot.apihelper.ApiException:
                pass


bot.polling(none_stop=True)