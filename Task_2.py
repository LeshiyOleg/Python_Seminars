#  2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#      Примеры:
    
#      - 1, 4, 8, 7, 5 -> 8
#      - 78, 55, 36, 90, 2 -> 90

# print ('Введите 5 чисел через клавишу Enter')

import random

list_numbers = []

for i in range(5):
    list_numbers.append(random.randint(1,100))
print(list_numbers)

# list_numbers = [1,2,3,4,5]
max_num = list_numbers[0]
for item in list_numbers:
    if item > max_num:
        max_num = item
print(max_num)