print('Введите число:')
number = int(input())

quantity = 0

if number % 2 == 0:
    while number // 2 and number // 2 > 2:
        number = number // 2
        quantity += 1

print(quantity)
