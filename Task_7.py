# 2. Напишите программу, которая будет 
# принимать на вход дробь и показывать 
# первую цифру дробной части числа.
    
# *Примеры:*
    
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3


import math

print ('Введите десятичную дробь')
number = float(input())
print(round(int(number*10%10)))