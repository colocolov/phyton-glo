print('¬ведите число:')
number = int(input())

summa = 0
total = 0

while number != 0:
    last_digit = number % 10
    summa = summa + last_digit
    number = number // 10
    if number == 0:
        while summa != 0:
            last_digit = summa % 10
            total = total + last_digit
            summa = summa // 10
            if total > 9:
                summa = total
                total = 0
                while summa != 0:
                    last_digit = summa % 10
                    total = total + last_digit
                    summa = summa // 10

print(total)