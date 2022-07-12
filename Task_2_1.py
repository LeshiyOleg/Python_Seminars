# print(week_days.keys())
# print(week_days.values())
# print(week_days.items())
# print(week_days[3])
# week_days['olga'] = 89650456534
# print(week_days)

# lst = list(range(1,8))
# while True:
#     number= input('введите цифру обозначающую день недели: ')
#     if not number.isdigit():
#         continue
#     elif number in lst:
#         break

week_days = {1:"Mon", 2:"Tue", 3:"Wed", 4:"Thu", 5:"Fri", 6:"Sat", 7:"Sun"}
checking = True
while checking:
    week_day_number = input('Enter day of a week: ')
    if week_day_number.isdigit():
        week_day_number = int(week_day_number)
        if week_day_number >=1 and week_day_number <= 7:
            checking = False
        else:
            print("There is no such day of a week --> Try again")
    else:
        print("Not a number --> Try again")

if week_day_number ==6 or week_day_number ==7:
    print(f"{week_day_number} {week_days[week_day_number]} --> Holiday")
else:
    print(f"{week_day_number} {week_days[week_day_number]} --> Working day")