# Задана натуральная степень n. Сформировать случайным образом список коэффициентов
#  (значения от 0 до 100) многочлена и записать в файл многочлен степени n. 
#  ```
#  Пример: 
#  n=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#  ```

from methods import check_value_is_positive_integer_and_return_it as input_number
# from methods import make_random_list_int_numbers_n_elements as random_list
import random

# Функция создает список из целых чисел в строковом представлении, запрашивает на вход 
# количество элементов, мин и макс элементы диапазона рандома.
def make_random_list_int_numbers_n_elements (elem_number:int, min_rand:int, max_rand:int):
    random_list_numbers = []
    for i in range(elem_number):
        random_list_numbers.append(str(random.randint(min_rand, max_rand)))
    return random_list_numbers

def get_polynomial_record(pow_value:int, min_coeff:int, max_coeff:int) -> str:
    result_list = []
    str_of_x = "x"
    pow_show_list = ["^"+str(i) for i in range(pow_value, 1, -1)]
    for i in range (2):
        pow_show_list.append("")
    print(f'pow_show {pow_show_list}')
    coefficients_list = make_random_list_int_numbers_n_elements(pow_value+1, min_coeff, max_coeff)
    print (f'initial coeff_list {coefficients_list}')
    if coefficients_list[0] == "0":
        coefficients_list[0] = str(random.randint(min_coeff+1, max_coeff))
    for i in range (0,len(coefficients_list)):
        if coefficients_list[i] == "1" and i<len(coefficients_list)-2:
            result_list.append(str_of_x + pow_show_list[i])
        elif coefficients_list[len(coefficients_list)-2] == "1":
            result_list.append(str_of_x)
        elif i == len(coefficients_list)-1 and coefficients_list[i] != "0":
            result_list.append(coefficients_list[i])
        elif coefficients_list[i] == "0":
            continue
        else:
            result_list.append(coefficients_list[i] + str_of_x + pow_show_list[i])
    print (f'result coeff_list {result_list}')
    result_string = str(result_list[0])
    for i in range (1, len(result_list)):
        result_string += " + " + result_list[i]
    result_string += " = 0"
    print (f'result coeff_list {result_string}')

pow_number = input_number('Input pow value to make a polynomial: ')
get_polynomial_record(pow_number, 0, 100)