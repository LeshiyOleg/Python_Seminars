import random

# функция проверки ввода целого положительного числа (N >= 0)
# со счетчиком неверных попыток ввода и автоматическим закрытием программы
# при их превышении

def check_value_is_positive_integer_and_return_it(input_value:str, limit:int = 3) -> int:
    count = 1
    while True:
        value = input(input_value)
        if value.isdigit():
            number = int(value)
            break
        elif count < limit:
            print(f"This is not correct number --> Try again\nYou have {limit-count} input attempts left")
            count += 1
        else:
            print("Exceeded number of input attempts. Think what you're doing wrong --> Closing the program")
            exit()
    return number


# функция проверки ввода целого числа (положительного или отрицательного)
# со счетчиком неверных попыток ввода и автоматическим закрытием программы
# при их превышении

def check_value_is_digit_and_return_it(input_value:str, limit:int = 3) -> int:
    checking_continue = True
    is_minus = False
    count = 1
    while checking_continue:
        value = input(input_value)
        if value[0] == "-":
            value = value.replace("-","")
            is_minus = True
        if value.isdigit():
            number = int(value)
            if is_minus:
                number *= -1
            checking_continue = False
        elif count < limit:
            print(f"This is not an integer number --> Try again\nYou have {limit-1-count} input attempts left")
            count += 1
        else:
            print("Exceeded number of input attempts. Think what you're doing wrong --> Closing the program")
            exit()
    return number

# Функция создает список из целых чисел, запрашивает на вход
# мин и макс элементы диапазона рандома. Тело функции запрашивает количество
# элементов в списке, а потом формирует его из рандомных элементов
def make_new_random_list_int_numbers (min_rand:int, max_rand:int):
    elem_number = check_value_is_digit_and_return_it ("Please input number of list elements: ")
    random_list_numbers = []
    for i in range(elem_number):
        random_list_numbers.append(random.randint(min_rand, max_rand))
    return random_list_numbers


# Функция создает список из вещественных чисел, запрашивает на вход мин и макс
# элементы диапазона рандома. Тело функции запрашивает количество элементов в
# списке, а потом формирует его из рандомных элементов
def make_new_random_list_real_numbers (min_rand:int, max_rand:int):
    elem_number = check_value_is_digit_and_return_it ("Please input number of list elements: ")
    random_list_numbers = []
    for i in range(elem_number):
        random_list_numbers.append(round(((random.random())*random.randint(min_rand, max_rand)), 3))
    return random_list_numbers


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

# функция сортирует список из целых чисел по возрастанию
def get_sorted_list (list_to_sort: list)-> list:
    k = 0
    while k<(len(list_to_sort)-1):
        for i in range(len(list_to_sort)-1):
            if list_to_sort[i] > list_to_sort[i+1]:
                list_to_sort[i], list_to_sort[i+1] = list_to_sort[i+1], list_to_sort[i]
        k +=1
    return list_to_sort


# функция конвертирует список в строку
def make_string_from_list (list_to_convert:list)->str:
    result_string = ""
    for i in range(len(list_to_convert)):
        if i< len(list_to_convert)-1:
            result_string += str(list_to_convert[i])+" "
        else:
            result_string += str(list_to_convert[i])
    return result_string

# функция счетчика неверных попыток ввода с автоматическим закрытием программы
# при их превышении 
def input_options (
                    opt_inquiry = 'Selection options',
                    opt_1 = 'Option_1 message.\n',
                    opt_2 = 'Option_2 message.\n'):
    
    count = 0
    while count < 3:
        option_value = check_value_is_digit_and_return_it (opt_inquiry)
        if option_value == 1:
            print (opt_1)
            break
        elif option_value == 2:
            print (opt_2)
            break
        else:
            print(f'Wrong input. You have {2-count} input attempts left ')
            count +=1
    return option_value


# Функция ограничения попыток неправильного ввода варианта опции
# В словарь записываются с индексами [0] - запрос, [1] - опция_1, [2] - опция_2 и т.д.
def invalid_input_limit (dictionary: dict, limit:int = 3) -> int:
    count = 0
    while count < limit:
        option_value = check_value_is_digit_and_return_it(dictionary[0])
        if 0 <= option_value < len(dictionary):
            if option_value == 1:
                print (dictionary[1])
                break
            elif option_value == 2:
                print (dictionary[2])
                break
            elif option_value == 3:
                print (dictionary[3])
                break    
        else:
            print(f'Неверный ввод. У вас осталось {2-count} попыток ввода')
            count +=1
    return option_value
