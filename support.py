import telebot

token = '6047538970:AAHrhmToo71XDJR4X78i5secVMHsK1KqO-M'
bot = telebot.TeleBot(token)
def T_support(user, user_appeal, support_answer):
    bot.send_message(user, f'{user_appeal}\nОтвет на Ваше обращение: {support_answer}\n')
data = open('appeals.txt', 'r', encoding='utf-8')
appeals_from_user = data.readlines()
data.close()

support_answers = []
for row in appeals_from_user:
    new_appeal = row.split('  ')
    user_appeal = new_appeal[1] 
    print(user_appeal[:-1])
    support_answer = input('Ответ на обращение:')
    T_support(new_appeal[0], new_appeal[1], support_answer)
    support_answers.append(row)
for support_answer in support_answers:
    appeals_from_user.remove(support_answer)
data = open('appeals.txt', 'w', encoding='utf-8')
data.writelines(appeals_from_user)
data.close()