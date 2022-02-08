print('Введите число или ноль для завершения ввода:')
number = int(input())

total = 0
quan_pl = 0
quan_ds = 0

while number != 0:
    if number > 0:
        quan_pl += 1
    else:
        quan_ds += 1
    total = quan_ds * quan_pl
    number = int(input())

print('--', total)
