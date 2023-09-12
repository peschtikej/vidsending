import telebot 
from telebot import types

bot = telebot.TeleBot('5912963181:AAEW7BJekrCuGwBD9hsIFTn-AUTfpxylpi8')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("захар.")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет", reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text=='захар.':
        video = open('vid.mp4', 'rb')
        bot.send_video(message.chat.id, video)
bot.polling()