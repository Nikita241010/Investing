import requests
import json
import telebot
from telebot import types

# Replace with your OpenRouter API key
API_KEY = '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'
API_URL = 'https://openrouter.ai/api/v1/chat/completions'

token = "7796348346:AAE5MxgCkbE-_thS3J7KDylJ_OyuZINkoNw"

bot = telebot.TeleBot(token)

person = ''
year = ''

def generate_answer(person, year):
    data = {
        "Илон Маск": {
            "2021": "Илон Маск в 2021",
            "2022": "Илон Маск в 2022",
            "2023": "Илон Маск в 2023",
            "2024": "Илон Маск в 2024",
            "2025": "Илон Маск в 2025"
        },
        "Дональд Трамп": {
            "2021": "Дональд Трамп в 2021",
            "2022": "Дональд Трамп в 2022",
            "2023": "Дональд Трамп в 2023",
            "2024": "Дональд Трамп в 2024",
            "2025": "Дональд Трамп в 2025"
        },
        "Питер Бранд": {
            "2021": "Питер Бранд в 2021",
            "2022": "Питер Бранд в 2022",
            "2023": "Питер Бранд в 2023",
            "2024": "Питер Бранд в 2024",
            "2025": "Питер Бранд в 2025"
        },
        "Паоло Ардоино": {
            "2021": "Паоло Ардоино в 2021",
            "2022": "Паоло Ардоино в 2022",
            "2023": "Паоло Ардоино в 2023",
            "2024": "Паоло Ардоино в 2024",
            "2025": "Паоло Ардоино в 2025"
        },
        "Майкл Сейлор": {
            "2021": "Майкл Сейлор в 2021",
            "2022": "Майкл Сейлор в 2022",
            "2023": "Майкл Сейлор в 2023",
            "2024": "Майкл Сейлор в 2024",
            "2025": "Майкл Сейлор в 2025"
        }
    }

    return data[person][year]


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Илон Маск', callback_data='button1')
    button2 = types.InlineKeyboardButton('Дональд Трамп', callback_data='button2')
    button3 = types.InlineKeyboardButton('Питер Бранд', callback_data='button3')
    button4 = types.InlineKeyboardButton('Паоло Ардоино', callback_data='button4')
    button5 = types.InlineKeyboardButton('Майкл Сейлор', callback_data='button5')
    

    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)

def generate_new_buttons():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton('2021', callback_data='new_button1'),
        types.InlineKeyboardButton('2022', callback_data='new_button2'),
        types.InlineKeyboardButton('2023', callback_data='new_button3'),
        types.InlineKeyboardButton('2024', callback_data='new_button4'),
        types.InlineKeyboardButton('2025', callback_data='new_button5')
    )
    return markup

def edit_keyboard(message, new_markup):
    try:
        bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=message.message_id, reply_markup=new_markup)
    except Exception as e:
        print(f"Ошибка при изменении клавиатуры: {e}")

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    global person, year
    if call.data == 'button1':
        person = 'Илон Маск'
        new_buttons = generate_new_buttons()
        edit_keyboard(call.message, new_buttons)
    elif call.data == 'button2':
        person = 'Дональд Трамп'
        new_buttons = generate_new_buttons()
        edit_keyboard(call.message, new_buttons)
    elif call.data == 'button3':
        person = 'Питер Бранд'
        new_buttons = generate_new_buttons()
        edit_keyboard(call.message, new_buttons)
    elif call.data == 'button4':
        person = 'Паоло Ардоино'
        new_buttons = generate_new_buttons()
        edit_keyboard(call.message, new_buttons)
    elif call.data == 'button5':
        person = 'Майкл Сейлор'
        new_buttons = generate_new_buttons()
        edit_keyboard(call.message, new_buttons)
    elif call.data == 'new_button1':  
        year = '2021'
        message = generate_answer(person, year)
        bot.send_message(call.message.chat.id, message)
    elif call.data == 'new_button2':  
        year = '2022'
        message = generate_answer(person, year)
        bot.send_message(call.message.chat.id, message)
    elif call.data == 'new_button3':  
        year = '2023'
        message = generate_answer(person, year)
        bot.send_message(call.message.chat.id, message)
    elif call.data == 'new_button4':  
        year = '2024'
        message = generate_answer(person, year)
        bot.send_message(call.message.chat.id, message)
    elif call.data == 'new_button5':  
        year = '2025'
        message = generate_answer(person, year)
        bot.send_message(call.message.chat.id, message)
        


bot.infinity_polling()
