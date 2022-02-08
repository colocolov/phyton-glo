print('Введите число. Чтобы прекратить ввод, введите число больше 100:')
number = int(input())

while number < 100:
    if number < 10:
        print('Введите число больше 10')
        number = int(input())
    elif number > 100:
        break
    else:
        print('Вы ввели', number)
        number = int(input())
