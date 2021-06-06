print('¬ведите текст:')

text = input()
numbers = ''
number = ''

for i in range(len(text)):
    symbol = ord(text[i])
    if symbol > 47 and symbol < 58:
        number = chr(symbol)
        numbers = numbers + number

print(numbers)


