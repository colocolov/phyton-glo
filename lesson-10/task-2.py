print('Введите символ:')
symbol = input()
code = ord(symbol)

if code > 47 and code < 58:
    print('YES')
else:
    print('NO')