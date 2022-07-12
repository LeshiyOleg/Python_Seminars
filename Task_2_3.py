# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
#     *Пример:*
    
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


elem_number = int(input('Введите число n элементов последовательности 3n + 1 : '))
dictionary = dict()
for i in range(1,elem_number+1):
    temp = 3*i +1
    dictionary[i] = temp
print (dictionary)