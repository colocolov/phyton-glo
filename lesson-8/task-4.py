print('Введите число больше 10:')
number = int(input())

maximum = 0
minimum = 10

if number > 9:
    while number != 0:
        last_digit = number % 10
        if last_digit > maximum:
            maximum = last_digit
        if last_digit < minimum:
            minimum = last_digit
        number = number // 10
    print('Минимальная цифра равна', minimum)
    print('Максимальная цифра равна', maximum)
else:
    print('Число должно быть больще 10!')
