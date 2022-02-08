print('Введите число:')
number = int(input())

flag = 1

if number == 0 or number == 1 or number == 2 or number == 3 or number == 5 or number == 7:
    flag = 1
else:
    for i in range(2, 10):
        if number % i == 0:
            flag = 0
            break

if flag == 0:
    print('NO')
else:
    print('YES')