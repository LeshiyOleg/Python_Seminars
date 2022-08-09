# Создать и заполнить файл случайными значениями. 
# Выполнить сортировку чисел в файле по возрастанию, 
# не используя sort или sorted

import random
from methods import check_value_is_digit_and_return_it as check

# функция создает список из рандомных целых чисел, конвертированных в строки, и записывает в файл
def get_list_of_numbers_as_str_and_write_in_file (number_N: int, file_name:str) -> list: 
    list_of_numbers = []
    for i in range(number_N):
        list_of_numbers.append(str(random.randint(0, 100)))
    file = open(file_name, 'w')
    file.write(" ".join(list_of_numbers))
    file.close()
    return list_of_numbers

# функция читает данные (целые числа) из файла и создает список из этих чисел
def take_values_from_file_and_make_numbers_list (file_name:str)-> list: 
    file = open(file_name, 'r')
    date = file.read()
    list_of_numbers = date.split()
    file.close()
    for i in range(len(list_of_numbers)):
        list_of_numbers[i] = int(list_of_numbers[i])
    return list_of_numbers

# функция сортирует список чисел по возрастанию
def get_sorted_list (list_to_sort: list)-> list:
    k = 0
    while k<(len(list_to_sort)-1):
        for i in range(len(list_to_sort)-1):
            if list_to_sort[i] > list_to_sort[i+1]:
                list_to_sort[i], list_to_sort[i+1] = list_to_sort[i+1], list_to_sort[i]
        k +=1
    return list_to_sort


number_N = check ('Input number of elements N to create a list: ')
list_of_numbers_in_file = get_list_of_numbers_as_str_and_write_in_file(number_N, 'file_2.txt')

print (list_of_numbers_in_file)
#print (take_values_from_file_and_make_numbers_list('file_2.txt'))
sorted_list = get_sorted_list(take_values_from_file_and_make_numbers_list('file_2.txt'))
print (sorted_list)

