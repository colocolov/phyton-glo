print('Введите количество чисел, которые хотите ввести:')
quantity = int(input())

flag = 0

for i in range(quantity):
    number = int(input())
    if number % 2 == 0:
        flag = flag + 1

if flag == 0:
    print('YES')
else:
    print('NO')
