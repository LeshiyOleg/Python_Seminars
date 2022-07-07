# 1. Напишите программу, которая будет на вход 
# принимать число N и выводить числа от -N до N
    
#*Примеры:* 
    
#- 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

print('Введите число N')
N = int(input())


if N>0:
    for index in range(N, -N-1, -1):
        print(index)
else:
    for index in range(N, -N+1, +1):
        print(index)


