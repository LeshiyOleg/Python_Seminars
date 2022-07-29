def check_value_is_digit_and_return_it(input_value:str):
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
        elif count < 3:
            print("This is not an integer number --> Try again")
            count += 1
        else:
            print("Exceeded number of input attempts. Think what you're doing wrong --> Closing the program")
            exit()
    return number

# def input_number_test(text):

#     int_test = True
#     is_minus = False
#     while int_test:
#         coord = input(f"{text}")
#         if coord[0] == "-":
#             is_minus = True
#             coord = coord.replace("-","")
#         if coord.isdigit():
#             coord = int(coord)
#             if is_minus:
#                 coord *= -1
#             int_test = False
#         else :
#             print("Not a number , try again")
#     return coord