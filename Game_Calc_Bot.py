import telebot
import random

token = 'TOKEN'
bot = telebot.TeleBot(token, parse_mode = None)

calculator = False
gamer = False
attempts = 0

@bot.message_handler(commands=['start','help','hello','calculator','game'])
def send_welcome(message):
    bot.reply_to(message, f"Привет, {message.from_user.first_name}! Хочешь посчитать или поиграть?")

@bot.message_handler(content_types = ['text'])
def echo_all(message):
    global calculator, result, gamer, answer_num, bot_num, attempts 
    culc = ['считать','ещё считать','калькулятор', 'хочу калькулятор', 'хочу посчитать', 'посчитать']
    game = ['играть','ещё играть', 'хочу играть', 'хочу поиграть', 'поиграть']
    if message.text in culc and calculator == False:
        bot.reply_to(message, f"Отлично, {message.from_user.first_name}, давай посчитаем! Введи выражение. Используй символ деления </>")
        calculator = True
    elif calculator == True:
        if message.text.isalpha():
            bot.reply_to(message, 'Ты же, вроде, посчитать собирался? Введи выражение')
        else:
            result = eval(message.text)
            bot.reply_to(message, f"Ответ: {result}")
            calculator = False
            bot.reply_to(message, f"{message.from_user.first_name}, Хочешь посчитать или поиграть?")   
    elif message.text in game and gamer == False:
        bot.reply_to(message, f"Отлично, {message.from_user.first_name}, давай поиграем!")
        gamer = True
        bot_num = random.randint(1, 1000)
        bot.reply_to(message, f"Угадай число от 1 до 1000")
    elif gamer == True:
        if message.text.isdigit():
            answer_num = int(message.text)
            attempts += 1
            if answer_num == bot_num:
                bot.reply_to(message, f'Вот это да! Ты угадал с {attempts} попытки! Это {answer_num}')
                gamer = False
                attempts = 0
            elif answer_num > bot_num:
                bot.reply_to(message, 'Я загадал меньше')
            else:
                bot.reply_to(message, 'Я загадал больше')
        else:
            bot.reply_to(message, 'Ты же, вроде, число отгадываешь?') 
        
bot.infinity_polling()
