print('Введите число:')
number = int(input())

flag = 0

while number != 0:
    last_digit = number % 10
    if last_digit == 1:
        flag = 1
        break
    number = number // 10

if flag == 0:
    print('NO')
else:
    print('YES')