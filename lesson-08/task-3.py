print('Введите число:')
number = int(input())

first_number = number
total = 0

while number != 0:
    last_digit = number % 10
    total += last_digit
    number = number // 10

if first_number % total == 0:
    print('YES')
else:
    print('NO')
    
