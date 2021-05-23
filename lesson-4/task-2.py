print('Введите первое число:')
number_one = int(input())
print('Введите второе число:')
number_two = int(input())
print('Вводятся два числа:', number_one, 'и', number_two)
print('Результаты вычислений:')
print(number_one, 'умноженное на', number_two, 'равно', number_one * number_two)
number_one_float = float(number_one)
number_two_float = float(number_two)
print(number_one_float, 'деленное на', number_two_float, 'равно', number_one / number_two)
print(number_one, 'нацело деленное на', number_two, 'равно', number_one // number_two)
print('Остаток от деления', number_one, 'на', number_two, 'равно', number_one % number_two)
print(number_one, 'в степени', number_two, 'равно', number_one ** number_two)

# 10 деленное на 4 равно 2.5
# 10 нацело деленное на 4 равно 2
# Остаток от деления 10 на 4 равно 2
# 10 в степени 4 равно 10000