# Пользователь вводит время в минутах и расстояние
# в километрах. Найдите скорость в м/c.

time_in_minutes = int(input('Введите время в минутах: '))
dist_in_km = int(input('Введите расстояние в километрах: '))

print(f'Скорость равняется {round((dist_in_km*1000)/(time_in_minutes*60),2)} м/с')
