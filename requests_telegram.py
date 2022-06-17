import requests
import telebot
from time import sleep

token = ''
bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda m: True)
def fox_images(message):
    
    response = requests.get('https://randomfox.ca/floof/')
    print(response.status_code)
    fox = response.json()
    
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, 'Aqui está a sua foto 🦊👇')
    bot.send_photo(message.chat.id, fox['image'])


          
while True:
    try:    
        bot.polling(none_stop=True)
    except:
        sleep(0.5)
        pass