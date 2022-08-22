#  Напишите программу вычисления арифметического выражения заданного строкой. 
#  Используйте операции +,-,/,*. приоритет операций стандартный.
# ```
# Пример:
# 2+2 => 4; 
# 1+2*3 => 7;
# 1-2*3 => -5;
# 10/2 * 5 => 25
# ```
#  Дополнительно: Добавьте возможность использования скобок, меняющих приоритет операций.
# ```
# Пример:
# 1+2*3 => 7
# (1+2)*3 => 9
# ```
# print(" ".join(list(filter(lambda word: 'абв' not in word, s.split()))))

# s = 'абвгдейка - это передача'
# def filter_text(text):
#     text = text.split(' ')
#     func = lambda word: 'абв' not in word
#     return ' '.join(list(filter(func, text)))
# print(filter_text(s))

def make_list_signs_digits (string_to_make:str)->list:
    math_signs = ['+', '-', '*', '/']
    signs = list(filter(lambda symbol: symbol in math_signs, list(string_to_make)))
    digits = []
    digit = ''
    string_to_make += ' '
    for i in range (len(string_to_make)):
        if string_to_make[i].isdigit():
            digit += string_to_make[i]
        else:
            digits.append(int(digit))    
            digit = ''
    return signs, digits

def make_operations(signs_and_digits):
    signs = signs_and_digits[0]
    digits = signs_and_digits[1]
    result = 0
    while len(signs) > 0:
        if '*' in signs:
            index = signs.index('*')
            result = digits[index] * digits[index+1]
        elif '/' in signs:
            index = signs.index('/')
            result = digits[index] / digits[index+1]
        elif '+' in signs:
            index = signs.index('+')
            result = digits[index] + digits[index+1]
        elif '-' in signs:
            index = signs.index('-')
            result = digits[index] - digits[index+1]
        signs.pop(index)
        digits[index+1] = result
        digits.pop(index)
    return result

def check_is_brackets (string_to_make):
    if '(' in string_to_make:
        result = get_result_in_brackets (string_to_make)
    else:
        result = make_operations(make_list_signs_digits(string_to_make))
    return result

def get_result_in_brackets (string_to_make):
    for i in range(len(string_to_make)-1, -1, -1):
        # print (i)
        # print(string_to_make[i])
        if string_to_make[i] == '(':
            string_brackets = ''
            index_open = i
            # print(index_open)
            break
    for j in range(index_open, len(string_to_make)):
        if string_to_make[j] == ')':
            index_close = j
            # print(index_close)
            break
    for k in range(index_open+1, index_close):
        string_brackets += string_to_make[k]
        # print(string_brackets)
    signs_and_digits_brack = make_list_signs_digits (string_brackets)
    result_brackets = make_operations(signs_and_digits_brack)
    new_string_to_make = string_to_make[:index_open] + str(result_brackets) + string_to_make[index_close+1:]
    # print(new_string_to_make)
    return check_is_brackets (new_string_to_make)


example_str = input ('Input expression: ')
signs_and_digits = check_is_brackets(example_str)


# signs_list = list(filter (lambda example: '+' in example, example_str.split()))
print(signs_and_digits)
