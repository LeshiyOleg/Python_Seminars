# Определить, присутствует ли в заданном списке 
# строк некоторое число

import random
from methods import check_value_is_digit_and_return_it as check

def find_number_in_list (list_of_numbers, input_number):
    flag = False
    for number in list_of_numbers:
        if number == input_number:
            flag = True             
            break
    if flag == True:
        print(f'{input_number} is in the list {list_of_numbers}')
    else:
        print(f'{input_number} is NOT in the list {list_of_numbers}')

input_number = check("Input a digit to find: ")

list_of_numbers = []
for i in range(1,10):
    list_of_numbers.append(random.randint(1,10))

find_number_in_list (list_of_numbers, input_number)

