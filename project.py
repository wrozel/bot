import telebot
from telebot import types
token='6981208017:AAH_13bb-WFx3On9Ab3BBEmAzld8tB-LDSI'
base_of_users=[]
base_of_questions=[]
base_of_answers=[]
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    global base_of_users, base_of_qusetions, base_of_answers
    user_id=message.from_user.username
    if user_id in base_of_users:
        k=base_of_users.index(user_id)
        base_of_users[k]=0
    base_of_users.append(user_id)
    base_of_questions.append([])
    base_of_answers.append([])
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Начать тест")
    markup.add(item1)
    item2=types.KeyboardButton("Добавить данные")
    markup.add(item2)
    bot.send_message(message.chat.id,'Привет, это бот для запоминания информации, которую Вам очень нужно выучить. Если Вы хотите быстро запомнить информацию, имея возможность проверить себя, то Вы обратились по адресу. Перед вами появились две кнопки. "Добавить данные" позволит Вам внести ваши вопросы и ответы к ним в базу программы. "Начать тест" предложит проверить Вас. Будьте внимательны: программа требует специальных обозначений при вводе сообщений, необходимых для использования бота. Вы увидите их, как только нажмете на кнопки. Желаем успехов в учебе!', reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):
    global base_of_users, base_of_questions, base_of_answers
    user_id=message.from_user.username
    index=base_of_users.index(user_id)
    if message.text=="Начать тест":
        s='Выберите вопрос, знание которого хотите проверить, для этого в начале вашего сообщения введите 0, напишите номер вопроса из следующего списка и поставьте пробел, затем в этом же сообщении введите ответ на вопрос, следующее сообщение от бота будет содержать правильный ответ:'
        for i in range(len(base_of_questions[index])):
            s+=base_of_questions[index][i]
        bot.send_message(message.chat.id,s)
    elif message.text=="Добавить данные":
        bot.send_message(message.chat.id,'Введите данные: первым сообщением добавьте вопрос, для этого перед началом ввода поставьте самым первым символом знак вопроса. После отправьте сообщение с ответом, но записав первым символом восклицательный знак')
    elif message.text[0]=="?":
        s=message.text[1::]
        s1=str(len(base_of_questions[index])+1)+"."
        a=s1+s
        base_of_questions[index].append(a)
    elif message.text[0]=="!":
        s=message.text[1::]
        s1=str(len(base_of_answers[index])+1)
        a=s1+s
        base_of_answers[index].append(a)
    elif message.text[0]=="0":
        t=message.text[1::]
        s0=""
        for i in t:
            if i!=" ":
                s0+=i
            else:
                break
        k=int(s0)
        try:
            t=base_of_answers[index][k-1]
            bot.send_message(message.chat.id, t[1::])
        except:
            bot.send_message(message.chat.id, "Вы ввели текст неправильно, перечитайте правила ввода и заново введите номер вопроса")
bot.infinity_polling()


