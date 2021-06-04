print('Введите число:')
number = int(input())

quantity = 0

for i in range(1, number + 1):
    last_digit = i % 10
    if last_digit == 5:
        quantity += 1

print(quantity)
