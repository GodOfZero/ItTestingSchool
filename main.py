import sqlite3
from sqlite3 import connect
import telebot
from telebot import types
import asyncio
bot = telebot.TeleBot('6105992511:AAHHw1UQ39NcZU0EewnCY8ZM-UtSmS5k5XE')
# мой id = 819119213
# id Инны = 424263646
# id Yulia = 170424502
# номер школи = 1134279105
admin_id = 819119213
ldata = '18 жовтня о 19:00'  # ldata='9 серпня о 19:00' не работает
DELAY_SECONDS = 5

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
    btn1 = types.InlineKeyboardButton(text="10-18 років", callback_data='10-18 років')
    btn2 = types.InlineKeyboardButton(text="18-40 років", callback_data='18-40 років')
    btn3 = types.InlineKeyboardButton(text="40-55+ років", callback_data='40-55+ років')

    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    video = open('Photo/v1s.mp4', 'rb')
    bot.send_message(message.chat.id,text='Перед тим, як пірнати у тестування, давай трішки познайомимось.\n\nМи допомагаємо людям опанувати професію QA і знайти свою першу роботу в IT з 2019 року. Вже більше 2500 наших випускників успішно працевлаштувались. \nСеред них люди від 15 до 60 років🫶\n\n<b>А скільки тобі років?</b>',
                   reply_markup=markup, parse_mode='html')
    # bot.send_video(message.chat.id, video,
    #                caption='Привіт👋🏼! \nВже зовсім скоро ми проведемо безкоштовне онлайн заняття з тестування ПЗ! \n\nКОЛИ? \n🗓 <b> 18 жовтня о 19:00 </b> \n\nДЕ? \n🔗 Посилання на заняття буде у цьому боті 📍 ближче до старту вебінару \n\nЦІЛЬ \n👨🏻‍💻 Дізнатися все про те, хто такий тестувальник та, що йому потрібно знати \n\nМи в Інстаграм:\nhttps://www.instagram.com/it_testing_school \n\nВиникли запитання?\n📞 +380 (99) 001 50 55\n💌 Або пишіть у Телеграм: @InnaTestingSchool',
    #                reply_markup=markup, parse_mode='html')

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == '10-18 років' or callback.data == '18-40 років' or callback.data == '40-55+ років':
        markup1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Новачок", callback_data='Новачок')
        btn2 = types.InlineKeyboardButton(text="Читав про IT", callback_data='Читав про IT')
        btn3 = types.InlineKeyboardButton(text="Проходив курси в іншій школі",
                                          callback_data='Проходив курси в іншій школі')
        markup1.add(btn1)
        markup1.add(btn2)
        markup1.add(btn3)
        bot.send_message(callback.message.chat.id , "Наша програма спрямована на початківців і максимально зрозуміла навіть для тих, хто раніше не мав досвіду в галузі IT. Вона також може бути корисною для більш досвідчених користувачів.\n\n<b>А який рівень твого досвіду в галузі IT?</b>" , reply_markup=markup1, parse_mode='html')
    if callback.data == 'Новачок' or callback.data == 'Читав про IT' or callback.data == 'Проходив курси в іншій школі':
        markup2 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Чат однодумців", url='https://t.me/+heo4d1d-2rRlNzAy',callback_data='Я все зробив')
        btn2 = types.InlineKeyboardButton(text="Наш сайт",url='https://it-testing-school.com/ua/programm', callback_data='Я все зробив')
        btn3 = types.InlineKeyboardButton(text="Наш ТГ-канал",callback_data='Я все зробив', url='https://t.me/freeittestingschool')
        btn4 = types.InlineKeyboardButton(text="Хочу навчатись!", callback_data='Я все зробив')
        markup2.add(btn1)
        markup2.add(btn2,btn3)
        markup2.add(btn4)
        file = open('Photo/v1s.mp4', 'rb')
        bot.send_video(callback.message.chat.id,file,
                         caption="<b>Дякуємо за відповіді! Твоя реєстрація на QA-вебінар пройшла успішно!</b>\nВже зовсім скоро ти дізнаєшся, що таке тестування і хто то такий, той QA-інженер💪\n\n<b>Стартуємо в середу 18 жовтня о 19:00 (за Києвом)</b>. На все про все 2 години. Ти поринеш у світ тестування, де можеш змінити буденну роботу на саму престижну професію в IT, з великими перевагами:\n\n💰 Зарплата від 600$\n🥰 Робота з будь-якої частини світу\n⏰ Гнучкий графік роботи\n❌ Без знань програмування\n✅ З початковим рівнем англійської\n🔥 Масажі, повне страхування, оплата спортзалу та багато іншого 👌🏼\n\nКОЛИ?\n🗓  <b>18 жовтня о 19:00</b>\n\nДЕ?\n🔗 Посилання на заняття буде у цьому боті 📍 ближче до старту вебінару\n\nЩоб тобі було не самотньо - приєднуйся до чату однодумців 👇🏼",
                         reply_markup=markup2,parse_mode='html')
    if callback.data == 'Я все зробив':
        markup3 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Посилання для друга", url='https://it-testing-school.com/ua/programm',
                                          callback_data='друг')
        markup3.add(btn1)
        bot.send_message(callback.message.chat.id,
                         "Бачимо, що ти дійсно зацікавлений в тому, щоб змінити своє життя.\n\n🔥<b>На вебінарі ти отримаєш студентську фінансову допомогу 💰!</b>\n\nЗапрошуй друзів, щоб проходити майстер-клас разом! ⬇️ ",
                         reply_markup=markup3, parse_mode='html')








@bot.message_handler(commands=['rassylkaY'])
def rassylka(message):
    if message.chat.id == admin_id:
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("SELECT id FROM login_id")
        user_ids = cursor.fetchall()
        for user_id in user_ids:
            with open('Photo/cs2.mp4', 'rb') as file:
             markup2 = types.InlineKeyboardMarkup()
             btn6 = types.InlineKeyboardButton(text="Посилання для друга",
                                              url="https://it-testing-school.com/ua/programm")
             btn1 = types.InlineKeyboardButton(text="Наш ТГ-канал", url="https://t.me/freeittestingschool")
             markup2.add(btn6)
             try:
                bot.send_video(user_id, file,
                               caption='Вже завтра о 19:00 ми проведемо для вас безкоштовний вебінар з тестування!\n\nОбовʼязково постав собі нагадування, щоб не пропустити головну подію цієї осені 🔥\n\nА також запрошуй друзів ⬇️',
                               reply_markup=markup2,parse_mode='html')
             except telebot.apihelper.ApiException:
                pass






@bot.message_handler(commands=['rassylka2dayss'])
def rassylka(message):
    if message.chat.id == admin_id:
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("SELECT id FROM login_id")
        user_ids = cursor.fetchall()
        for user_id in user_ids:
            file = open('Photo/cs2.mp4', 'rb')
            markup2 = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="Сергій",
                                              url="https://youtu.be/WlYiWeX1FG4")
            btn2 = types.InlineKeyboardButton(text="Олексій", url="https://youtu.be/wk00dx8pF_Y")
            btn3 = types.InlineKeyboardButton(text="Микита", url="https://youtu.be/Y6yJfnft6e0?si=mLkNMLsEetqRiTed")
            btn4 = types.InlineKeyboardButton(text="Влада", url="https://youtu.be/yG5cdtvTpUE")
            markup2.add(btn1)
            markup2.add(btn2)
            markup2.add(btn3)
            markup2.add(btn4)
            try:
                bot.send_video(user_id, file,
                               caption='Вже через завтра ти поринеш в самий довгоочікуваний вебінар цієї осені 🔥\n\nТому, хочемо трішки підготувати тебе до нього 👌🏼\n\nНаші випускники вже готові поділитися з тобою своїм досвідом закінчення курсу QA з нуля та старту роботи в айті 😍',
                               reply_markup=markup2,parse_mode='html')
            except telebot.apihelper.ApiException:
                pass


















































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
            btn6 = types.InlineKeyboardButton(text="🖇️Посилання на безкоштовне заняття",
                                              url="https://us02web.zoom.us/j/81419393460")
            btn1 = types.InlineKeyboardButton(text="Наш ТГ-канал", url="https://t.me/freeittestingschool")
            markup2.add(btn6)
            markup2.add(btn1)
            try:
                bot.send_video(user_id, file,
                               caption='❗️ Майже 30 хвилин до прямого ефіру.\nДе ми розповімо: \n \n😮 Як без досвіду в ІТ отримати роботу\n😮 Незалежно вам 15 чи 50 років\n😮 Працювати віддалено з дому\n😮 Як стабільно заробляти 1000$\n\n❌ Цю інформацію ніхто не розкаже!\n\n❗️ Через 30 хвилин ми розпочинаємо!',
                               reply_markup=markup2,parse_mode='html')
            except telebot.apihelper.ApiException:
                pass
#
#
# @bot.message_handler(commands=['rassylka60'])
# def rassylka(message):
#     if message.chat.id == admin_id:
#         connect = sqlite3.connect('users.db')
#         cursor = connect.cursor()
#         cursor.execute("SELECT id FROM login_id")
#         user_ids = cursor.fetchall()
#         for user_id in user_ids:
#             markup2 = types.InlineKeyboardMarkup()
#             btn1 = types.InlineKeyboardButton(text="Наш ТГ-канал", url="https://t.me/freeittestingschool")
#             btn2 = types.InlineKeyboardButton(text="Наш сайт", url="https://it-testing-school.com/ua")
#             markup2.add(btn2)
#             markup2.add(btn1)
#             file = open('Photo/v60.mp4', 'rb')
#             try:
#                 bot.send_video(user_id, file, caption='<b>Вам теж цікаве тестування, але в голові купа питань і '
#                                                       'сумнівів?</b> \n\nПриміряйте на себе професію QA Engineer вже '
#                                                       '<b><u>за годину</u></b> 🔥', reply_markup=markup2,parse_mode='html')
#             except telebot.apihelper.ApiException:
#                 pass
#
#
# @bot.message_handler(commands=['rassylka5'])
# def rassylka(message):
#     if message.chat.id == admin_id:
#         connect = sqlite3.connect('users.db')
#         cursor = connect.cursor()
#         cursor.execute("SELECT id FROM login_id")
#         user_ids = cursor.fetchall()
#         for user_id in user_ids:
#             file = open('Photo/v5.mp4', 'rb')
#             markup2 = types.InlineKeyboardMarkup()
#             btn6 = types.InlineKeyboardButton(text="🖇️Посилання на безкоштовне заняття",url="https://us02web.zoom.us/j/81419393460")
#             markup2.add(btn6)
#             try:
#                 bot.send_video(user_id, file,
#                                caption='🔊<b> Стартуємо через 5 хвилин! </b>Скоріше підкючайся, щоб нічого не пропустити \n\nПосилання на заняття: 👇🏼👇🏼👇🏼',reply_markup=markup2, parse_mode='html')
#             except telebot.apihelper.ApiException:
#                 pass
#
# @bot.message_handler(commands=['rassylka'])
# def rassylka(message):
#     if message.chat.id == admin_id:
#         connect = sqlite3.connect('users.db')
#         cursor = connect.cursor()
#         cursor.execute("SELECT id FROM login_id")
#         user_ids = cursor.fetchall()
#         for user_id in user_ids:
#             file = open('Photo/vrassylka.mp4', 'rb')
#             markup2 = types.InlineKeyboardMarkup()
#             btn1 = types.InlineKeyboardButton(text="Наш ТГ-канал", url="https://t.me/freeittestingschool")
#             btn2 = types.InlineKeyboardButton(text="Наш сайт", url="https://it-testing-school.com/ua")
#             markup2.add(btn2)
#             markup2.add(btn1)
#             try:
#                 bot.send_video(user_id, file,
#                                caption='<b>Сьогодні о 19:00</b> в онлайні розкажемо:\n✅ як можна заробляти з дому маючи ПК та інтернет\n✅ як отримати високоплачувану віддалену професію\n✅ як працевлаштуватись без досвіду\n✅ як отримати 1000$ на місяць\n\n<b>P.S. 🖇<i> Посилання на заняття буде ближче до старту вебінару сьогодні до 19:00</i></b>',
#                                parse_mode='html', reply_markup=markup2)
#             except telebot.apihelper.ApiException:
#                 pass
#
#
# @bot.message_handler(commands=['rassylka120'])
# def rassylka(message):
#     if message.chat.id == admin_id:
#         connect = sqlite3.connect('users.db')
#         cursor = connect.cursor()
#         cursor.execute("SELECT id FROM login_id")
#         user_ids = cursor.fetchall()
#         for user_id in user_ids:
#             file = open('Photo/v120.mp4', 'rb')
#             markup2 = types.InlineKeyboardMarkup()
#             btn1 = types.InlineKeyboardButton(text="Наш ТГ-канал", url="https://t.me/freeittestingschool")
#             btn2 = types.InlineKeyboardButton(text="Наш сайт", url="https://it-testing-school.com/ua")
#             markup2.add(btn2)
#             markup2.add(btn1)
#
#             try:
#                 bot.send_video(user_id, file,
#                                caption='<b>Через 2 години відбудеться захоплююче заняття з тестування ПЗ 🥳🥳🥳</b> \n\n<i>Підготуйтеся до нових викликів та поглиблення знань 😉</i>',
#                                reply_markup=markup2, parse_mode='html')
#             except telebot.apihelper.ApiException:
#                 pass
#
#
# @bot.message_handler(commands=['rassylkastart'])
# def rassylka(message):
#     if message.chat.id == admin_id:
#         connect = sqlite3.connect('users.db')
#         cursor = connect.cursor()
#         cursor.execute("SELECT id FROM login_id")
#         user_ids = cursor.fetchall()
#         for user_id in user_ids:
#             file = open('Photo/vstart.mp4', 'rb')
#             markup2 = types.InlineKeyboardMarkup()
#             btn6 = types.InlineKeyboardButton(text="🖇️Посилання на безкоштовне заняття",
#                                               url="https://us02web.zoom.us/j/81419393460")
#             markup2.add(btn6)
#             try:
#                 bot.send_video(user_id, file,
#                                caption='🔊<b> Хутчіше підключайся!</b>\n\nПосилання на заняття: 👇🏼👇🏼👇🏼',
#                                reply_markup=markup2,parse_mode='html')
#             except telebot.apihelper.ApiException:
#                 pass
#
#
# @bot.message_handler(commands=['rassylkapromo'])
# def rassylka(message):
#     if message.chat.id == admin_id:
#         connect = sqlite3.connect('users.db')
#         cursor = connect.cursor()
#         cursor.execute("SELECT id FROM login_id")
#         user_ids = cursor.fetchall()
#         for user_id in user_ids:
#             file = open('Photo/vpromo.mp4', 'rb')
#             markup2 = types.InlineKeyboardMarkup()
#             btn6 = types.InlineKeyboardButton(text="🖇️Посилання на безкоштовне заняття",
#                                               url="https://us02web.zoom.us/j/81419393460")
#             btn2 = types.InlineKeyboardButton(text="Наш сайт", url="https://it-testing-school.com/ua")
#             markup2.add(btn6)
#             markup2.add(btn2)
#             try:
#                 bot.send_video(user_id, file,
#                                caption='Тільки сьогодні вас очікує <b>промокод на супер знижку</b> 🔥🔥🔥\nНе пропустіть!',
#                                reply_markup=markup2,
#                                parse_mode='html')
#             except telebot.apihelper.ApiException:
#                 pass
#
#
# @bot.message_handler(commands=['rassylkaoplata'])
# def rassylka(message):
#     if message.chat.id == admin_id:
#         connect = sqlite3.connect('users.db')
#         cursor = connect.cursor()
#         cursor.execute("SELECT id FROM login_id")
#         user_ids = cursor.fetchall()
#         for user_id in user_ids:
#             file = open('Photo/voplata.mp4', 'rb')
#             markup2 = types.InlineKeyboardMarkup()
#             btn6 = types.InlineKeyboardButton(text="Придбати курс",
#                                               url="https://it-testing-school.com/ua/pay-for-qamanual")
#             markup2.add(btn6)
#             try:
#                 bot.send_video(user_id, file,
#                                caption='<b>Ціна курсу зі знижкою 14600 грн.</b> \nТакож є оплата частинами\nДо 09.08 - 7300 грн\nДо 16.08 - 7300 грн\n\n🎁 <b>Сплатити курс можна за прямим посиланням: </b>👇🏼👇🏼👇🏼👇🏼👇🏼',
#                                reply_markup=markup2,
#                                parse_mode='html')
#             except telebot.apihelper.ApiException:
#                 pass
# @bot.message_handler(commands=['rassylkazapis'])
# def rassylka(message):
#     if message.chat.id == admin_id:
#         connect = sqlite3.connect('users.db')
#         cursor = connect.cursor()
#         cursor.execute("SELECT id FROM login_id")
#         user_ids = cursor.fetchall()
#         for user_id in user_ids:
#             file = open('Photo/vzapis.mp4', 'rb')
#             markup2 = types.InlineKeyboardMarkup()
#             btn6 = types.InlineKeyboardButton(text="Переглянути запис",url="https://it-testing-school.com/ua/pay-for-qamanual")
#             btn2=types.InlineKeyboardButton(text="Наш сайт",
#                                                                               url="https://it-testing-school.com/ua/programm")
#             btn4 = types.InlineKeyboardButton(text="Придбати курс",
#                                               url="https://it-testing-school.com/ua/pay-for-qamanual")
#
#             markup2.add(btn6)
#             markup2.add(btn2,btn4)
#             try:
#                 bot.send_video(user_id,file,
#                                caption="Доброго дня! 🤗\nВчора у нас відбулось безкоштовне заняття з  тестування ПЗ. Надаємо вам доступ до запису заняття: 👇🏼👇🏼👇🏼\n\n🔥🔥🔥 https://bit.ly/3E9OlrS 🔥🔥🔥\n\n<b>Наступний курс стартує 9 листопада</b>\nКурс складається із 22 занять\nРозклад: пн. 19:00, чт. 19:00 (за Києвом)\nРівень: з нуля\nМова викладання: українська\nФормат навчання: онлайн з записом занять\n\nТільки для вас діє знижка на курс з тестування ПЗ за промокодом <b>SLAVAUKRAINI 🇺🇦 за 14899 грн</b>\n\nТакож є оплата частинами:\nдо 09.10 - 7450 грн\nдо 09.11 -  7449 грн\n\nВиникли запитання?\n📞 +380 (99) 001 50 55\n💌 Або пишіть у Телеграм: @InnaTestingSchool",
#                                reply_markup=markup2,
#                                parse_mode='html')
#             except telebot.apihelper.ApiException:
#                 pass
#
# @bot.message_handler(commands=['rassylkalastday'])
# def rassylka(message):
#     if message.chat.id == admin_id:
#         connect = sqlite3.connect('users.db')
#         cursor = connect.cursor()
#         cursor.execute("SELECT id FROM login_id")
#         user_ids = cursor.fetchall()
#         for user_id in user_ids:
#             file = open('Photo/vlastday.mp4', 'rb')
#             markup2 = types.InlineKeyboardMarkup()
#             btn6 = types.InlineKeyboardButton(text="Переглянути запис",url="https://it-testing-school.com/ua/pay-for-qamanual")
#             btn2=types.InlineKeyboardButton(text="Наш сайт",
#                                                                               url="https://it-testing-school.com/ua/programm")
#             btn4 = types.InlineKeyboardButton(text="Придбати курс",
#                                               url="https://it-testing-school.com/ua/pay-for-qamanual")
#
#
#             markup2.add(btn2,btn4)
#             try:
#                 bot.send_video(user_id,file,
#                                caption="<b>ОСТАННІЙ ДЕНЬ ЗНИЖКИ НА КУРС</b>\n\nБільше такого <b>не буде</b>!",
#                                reply_markup=markup2,
#                                parse_mode='html')
#             except telebot.apihelper.ApiException:
#                 pass
#
# @bot.message_handler(commands=['rassylka36'])
# def rassylka(message):
#     if message.chat.id == admin_id:
#         connect = sqlite3.connect('users.db')
#         cursor = connect.cursor()
#         cursor.execute("SELECT id FROM login_id")
#         user_ids = cursor.fetchall()
#         for user_id in user_ids:
#             file = open('Photo/v36.mp4', 'rb')
#             markup2 = types.InlineKeyboardMarkup()
#             btn6 = types.InlineKeyboardButton(text="Переглянути запис",url="https://it-testing-school.com/ua/pay-for-qamanual")
#             btn2=types.InlineKeyboardButton(text="Наш сайт",
#                                                                               url="https://it-testing-school.com/ua/programm")
#             btn4 = types.InlineKeyboardButton(text="Придбати курс",
#                                               url="https://it-testing-school.com/ua/pay-for-qamanual")
#
#
#             markup2.add(btn2,btn4)
#             try:
#                 bot.send_video(user_id,file,
#                                caption="<b>ЗАЛИШИЛОСЬ 36 ГОДИН</b>\nВстигни придбати курс з тестування з максимальною вигодою <b>за 14900 грн!\n</b>Ціна на курс вже не буде такою <b>НІКОЛИ</b>.\n\n+380 (63) 519 33 19 ",
#                                reply_markup=markup2,
#                                parse_mode='html')
#             except telebot.apihelper.ApiException:
#                 pass

bot.polling(none_stop=True)
