print('Введите число не превосходящее 1 000 000 000:')
number = int(input())
digit_one = number % 1000 // 100
digit_two =  number % 100 // 10
digit_three = number % 10
sum = digit_one + digit_two + digit_three
print('Ввод', number)
print('У числа', number, 'сумма последних трех цифр равна', sum)