print('Введите символ:')
symbol = input()
code = ord(symbol)

if code > 64 and code < 91:
    code = code + 32
    symbol = chr(code)
elif code > 96 and code < 123:
    code = code - 32
    symbol = chr(code)    

print(symbol)
