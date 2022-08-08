# 1) в виде команды (/add 2 4)
# 2) в виде команды, но передается целое выражение
# 3) выражение в виде сообщения

def add(update, context):
    arg = context.args
    print (arg)
    try:
        arg = list(map(int,arg))
    except ValueError:
        context.bot.send_message(update.effective_chat.id, "Вы ввели не число")
    result = sum(arg)
    arg = "+".join(list(map(str, arg)))
    context.bot.send_message(update.effective_chat.id, f"{arg} = {result}")
    # sum = 0
    # for i in range (len(arg)):
    #     if arg[i].isdigit:
    #         num = int(arg[i])
    #         sum += num
    # print (sum)

def count(update, context):
    number_1 = update.message.text
    try:
        eval(number_1)
        context.bot.send_message(update.effective_chat.id, f"Test {number_1}")
    except:
        context.bot.send_message(update.effective_chat.id, f"Попробуйте ввести что-то другое")

def start(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Привет")
    else:
        context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")


def info(update, context):
    context.bot.send_message(update.effective_chat.id, "I'm Batman")


def message(update, context):
    text = update.message.text
    if text.lower() == 'привет':
        context.bot.send_message(update.effective_chat.id, 'И тебе привет..')
    else:
        context.bot.send_message(update.effective_chat.id, 'я тебя не понимаю')


def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, f'Шо сказал, не пойму')

