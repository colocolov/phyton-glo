print('Введите два числа:')
number_one = int(input())
number_two = int(input())

if number_one > number_two:
    digist_three = number_two
    digist_four = number_one
    number_one = digist_three
    number_two = digist_four

print('Результат:')
for i in range(number_one, number_two + 1, 1):
    if_zero = number_one % 2
    if if_zero == 0:
        print(number_one)
    number_one = number_one + 1