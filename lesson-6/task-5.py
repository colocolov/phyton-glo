print('Введите ваш емайл:')
email = input()

if '@' and '.' in email:
    print('Корректный')
else:
    print('Некорректный')