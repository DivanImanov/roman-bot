import telebot 
import roman_converter

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Greeting text')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if roman_converter.direction(message.text) != 'Error':
        bot.send_message(message.chat.id, roman_converter.direction(message.text))
    elif roman_converter.direction(message.text) == 'Error':
        bot.send_photo(message.chat.id, 'https://www.freeiconspng.com/uploads/sign-error-icon-10.png', caption='Error!')

bot.polling(none_stop=True, interval=0)
