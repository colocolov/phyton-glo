print('Введите символ:')
symbol = input()
code = ord(symbol)

if code > 1039 and code < 1072:
    print('YES')
else:
    print('NO')