# 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

first_str = "Говорит попугай попугаю: Я тебя, попугай, попугаю. Отвечает ему попугай:. Попугай, попугай, попугай!"
second_str = 'Попуг'
first_str = first_str.lower()
second_str = second_str.lower()

amount = 0
for i in range(len(first_str) - len(second_str)):
    if first_str[i:i + len(second_str)] == second_str:
        amount += 1

print(amount)
