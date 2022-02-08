print('Введите число:')
number = int(input())

print('Результат:')
for i in range(1, 11, 1):
    result = number * i
    print(number, 'x', i, '=', result)
