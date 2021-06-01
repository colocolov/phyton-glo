print('Введите число:')
number_one = int(input())

two = 1
nine = 1

if number_one < 2:
    print(0)
else:
    for i in range(1, number_one + 1, 1):
        if (i % 10) == 2:
            two = two * i
        elif (i % 10) == 9:
            nine = nine * i

    print('Результат:', two * nine)
