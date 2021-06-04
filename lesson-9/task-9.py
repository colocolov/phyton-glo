print('Введите число:')
number = int(input())

quantity = 0
summa = 0
total = 0

while number != 0:
    last_digit = number % 10
    summa = summa + last_digit
    number = number // 10

while summa != 0:
    last_digit = summa % 10
    total = total + last_digit
    summa = summa // 10

print(summ)
