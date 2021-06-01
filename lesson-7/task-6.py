print('Введите число:')
number_one = int(input())

one = 0
three = 0
seven = 0

for i in range(1, number_one + 1, 1):
    if (i % 10) == 1:
        one = one + i
    elif (i % 10) == 3:
        three = three + i
    elif (i % 10) == 7:
        seven = seven + i

print('Результат:', one + three + seven)
