print('Введите трехзначное положительное число:')
number = int(input())
digit_one = number // 100
digit_two = number % 100 // 10
digit_three = number % 10
print('Сумма цифр числа', number, 'равна', digit_one + digit_two + digit_three)
print('Произведение цифр числа', number, 'равно', digit_one * digit_two * digit_three)
