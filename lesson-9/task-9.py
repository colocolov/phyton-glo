print('¬ведите число:')
number = int(input())

summa = 0
total = 0
total2 = 0

while number != 0:
    last_digit = number % 10
    summa = summa + last_digit
    number = number // 10

while summa != 0:
    last_digit = summa % 10
    total = total + last_digit
    summa = summa // 10
    if total > 10:
        while total != 0:
            last_digit = total % 10
            total2 = total2 + last_digit
            total = total // 10
        total = total2

print(total)
