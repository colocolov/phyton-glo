print('Введите четырехзначное число:')
number = int(input())
digit_one = number // 1000
digit_two =  number % 1000 // 100
digit_three = number % 100 // 10
digit_four = number % 10
max_digit = max (digit_one, digit_two, digit_three, digit_four)
print('Ввод', number)
print('У числа', number, 'максимальная цифра равна', max_digit)