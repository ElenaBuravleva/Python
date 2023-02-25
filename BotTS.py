import telebot


token = '6047538970:AAHrhmToo71XDJR4X78i5secVMHsK1KqO-M'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, "Добрый день! Вы обратились в техподдержку. Чтобы оставить обращение, введите /appeal")


@bot.message_handler(commands=['appeal'])
def appeal_to_support(message):
    bot.reply_to(message, 'Ваш вопрос будет передан оператору. Введите его:')
    bot.register_next_step_handler(message, appeal_to_support)

def appeal_to_support(message):
    data = open('appeals.txt', 'a',encoding='utf-8')
    data.write(f'{message.from_user.id}  {message.from_user.first_name} {message.from_user.last_name}: {message.text}\n')
    data.close()
    bot.reply_to(message, 'Ваш вопрос передан оператору. Спасибо за обращение!')
        
bot.infinity_polling()