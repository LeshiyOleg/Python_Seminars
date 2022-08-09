# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

from methods import make_new_random_list_int_numbers as give_me_numbers

def make_string_from_list (list_to_convert:list)->str:
    result_string = ""
    for i in range(len(list_to_convert)):
        if i< len(list_to_convert)-1:
            result_string += str(list_to_convert[i])+" "
        else:
            result_string += str(list_to_convert[i])
    return result_string


def find_max_min_in_string (string_to_find:str)->int:
    list_to_find = string_to_find.split(" ")
    max = int(list_to_find[0])
    min = int(list_to_find[0])
    for i in range(1, len(list_to_find)):
        if list_to_find[i].isdigit:
            list_to_find[i] = int(list_to_find[i])
            if list_to_find[i]>max:
                max = int(list_to_find[i])
            if list_to_find[i]<min:
                min = int(list_to_find[i])
        else:
            print('Data in string is not correct --> Closing the program')
            exit()
    print (f'The maximal element in the string is: {max}')
    print (f'The minimal element in the string is: {min}')

numbers_list = give_me_numbers(-100, 100)
numbers_string = make_string_from_list(numbers_list)

print (f'The string with numbers: {numbers_string}')

find_max_min_in_string(numbers_string)