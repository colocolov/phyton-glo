print('Введите число:')
number = int(input())
digit_one = number % 2

#print(digit_one)

if digit_one == 0 and number != 2:
    print('YES')
else:
    print('NO')
