print('Введите число:')
number = int(input())

quantity = 0

while number != 0:
    last_digit = number % 10
    if last_digit == 5:
        quantity += 1
    number = number // 10

print(quantity)
