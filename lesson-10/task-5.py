print('¬ведите две буквы:')

symbol_one = input()
symbol_two = input()
code_one = ord(symbol_one)
code_two = ord(symbol_two)

print('Ѕуквы алфавита:')
if code_two > code_one:
    for i in range(code_one, code_two + 1):
        symbol = chr(i)
        print(symbol)
else:
    for i in range(code_two, code_one + 1):
        symbol = chr(i)
        print(symbol)       


