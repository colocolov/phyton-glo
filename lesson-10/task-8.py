print('Введите текст:')
text = input()

flag = 0
element = text[0]

for i in range(1, len(text)):
    symbol = text[i]
    if symbol == element:
        flag += 1
    else:
        element = symbol

print('Повторяющихся символов:', flag)

