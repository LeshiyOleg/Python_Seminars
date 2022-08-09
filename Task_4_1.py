# Задать список из N элементов, заполненных 
# числами из [-N, N]. Найти произведение элементов 
# на указанных позициях. Позиции хранятся в 
# файле file.txt в одной строке одно число

print ('You have already done this Task. Please look at Task_3_3!!!')

# import random
# from methods import check_value_is_digit_and_return_it as check


# def get_list_of_numbers(number_N):
#     list_of_numbers = []
#     for i in range(number_N):
#         list_of_numbers.append(random.randint(-number_N, number_N))
#     return list_of_numbers


# def find_mult_of_elem(list_of_numbers, list_of_raws):
#     result = 1
#     for item in list_of_raws:
#         #if item.isdigit():
#         try:
#             int(item)
#             item = int(item)
#             if item < len(list_of_numbers):
#                 result *= list_of_numbers[item]
#         #else:
#         except:
#             result = print('Data in file is not correct --> Closing the program')
#             exit()
#     return result

# number_N = check ('Input number of elements N to create a list: ')
# list_of_numbers = get_list_of_numbers(number_N)

# file = open('file_1.txt' , "r")
# data = file.read()
# list_of_raws = data.split()
# file.close()

# print(list_of_numbers)
# print(list_of_raws)

# mult_result = find_mult_of_elem (list_of_numbers, list_of_raws)

# print(f'The result of multiply of list elements {list_of_numbers} with indexes {list_of_raws} is {mult_result}')

