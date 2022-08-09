# Найдите НОК (наименьшее общее кратное) двух чисел

def find_min_common_multiple (number_1:int, number_2:int)-> int:
    if number_1>number_2:
        numb_to_check = number_1
    else:
        numb_to_check = number_2
    flag = False
    while flag == False:
        if numb_to_check % number_1 == 0 and numb_to_check % number_2 == 0:
            flag = True
        else:
            numb_to_check += 1
    return numb_to_check

print(find_min_common_multiple (4,3))
    