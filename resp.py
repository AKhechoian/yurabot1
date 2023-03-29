import telebot
import time
from telebot.types import Message


bot = telebot.TeleBot("5322804948:AAEqx_UgJi1v2YVTCdpCrhOWZ82yCJ-wweU")

# Replace 'chat_id' with '@sneakersteals-chat' for chat, @orsenbotchat for test
channel_name = '@orsenbotchat'
last_triggered_time = {}
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global last_triggered_time
    current_time = time.time()
    chat_id = message.chat.id
    if chat_id not in last_triggered_time or (current_time - last_triggered_time[chat_id]) > 60:
        if 'найк' in message.text.lower(): #if you want to trigger when the word is present in the message
            last_triggered_time[chat_id] = current_time
            bot.reply_to(message, "лучше посмотри в сторону Асикса. Есть отличные модели от Ронни Файга с интересными цветовыми решениями")
        elif message.text.lower() == 'слава украине': #the message should be exactly like that
            chat_id = message.chat.id
            last_triggered_time[chat_id] = current_time
            bot.reply_to(message, "ГЕРОЯМ СЛАВА")
        elif 'бородулин' in message.text.lower():
            chat_id = message.chat.id
            last_triggered_time[chat_id] = current_time
            bot.reply_to(message, "Идите..., хоронили уже меня, эвтаназия, вы поехавшие, я зла никогда никому не желал")
        elif 'как дела' in message.text.lower():
            chat_id = message.chat.id
            last_triggered_time[chat_id] = current_time
            bot.reply_to(message, "Дела у прокурора, у нас делишки всего лишь")
        elif 'рустэм' in message.text.lower():
            chat_id = message.chat.id
            last_triggered_time[chat_id] = current_time
            bot.reply_to(message, "Егор и Рустэм - основатели")
        elif 'русский' in message.text.lower():
            chat_id = message.chat.id
            last_triggered_time[chat_id] = current_time
            bot.reply_to(message, "Стыдно быть русским к сожалению")
        elif message.text.lower() == 'асикс лучше':
            chat_id = message.chat.id
            last_triggered_time[chat_id] = current_time
            bot.reply_to(message, "Солидарен, асикс 💪")
        elif message.text.lower() == 'хам':
            chat_id = message.chat.id
            last_triggered_time[chat_id] = current_time
            bot.reply_to(message, "@hamoffnick, летит полнейший респект")
        elif message.text.lower() == 'не скидывает':
            chat_id = message.chat.id
            last_triggered_time[chat_id] = current_time
            bot.reply_to(message, "пусть вокруг очка понюхает и в буруны носиком потолкается")
        elif 'торг' in message.text.lower():
            chat_id = message.chat.id
            last_triggered_time[chat_id] = current_time
            bot.reply_to(message, "Цены и так низкие, оскорбление просить ещё торг")
        elif 'фильм' in message.text.lower():
            chat_id = message.chat.id
            last_triggered_time[chat_id] = current_time
            bot.reply_to(message, "Кто не смотрел улицы разбитых фонарей, убойная сила, агент национальной безопасности, бандитский петербург, бригаду, можно лишать гражданства российского")
        elif 'сникершот' in message.text.lower():
            chat_id = message.chat.id
            last_triggered_time[chat_id] = current_time
            bot.reply_to(message, "Отчасти сникершот многих из нас породил")
        elif 'оставить' in message.text.lower():
            chat_id = message.chat.id
            last_triggered_time[chat_id] = current_time
            bot.reply_to(message, "В РФ бессмысленно оставлять, это к сожалению не данки или иордания 1")
        elif 'приоритет' in message.text.lower():
            chat_id = message.chat.id
            last_triggered_time[chat_id] = current_time
            bot.reply_to(message, "Приоритет всегда в РФ пару оставить")

bot.polling(timeout=None)
