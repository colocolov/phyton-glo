print('Введите число:')
number = int(input())

summa = 0
total = 0

while number != 0:
    last_digit = number % 10
    summa = summa + last_digit
    number = number // 10
    if number == 0 and summa > 9:
        number = summa
        summa = 0
print('Сумма чисел', summa)
