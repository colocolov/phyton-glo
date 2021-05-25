print('Введите число:')
number = int(input())

digit_one = number % 2

#print(digit_one)

if number > 0 and number <= 36:
    if (number >= 1 and number <= 10) or (number >= 19 and number <= 28):
        if digit_one == 0:
            print('черный')
        else:
            print('красный')
    else:
        if digit_one == 0:
            print('красный')
        else:
            print('черный')
elif number == 0:
    print('зеленый')
else:
    print('ошибка ввода')
