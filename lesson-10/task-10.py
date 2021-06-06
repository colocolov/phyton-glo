print('Введите текст:')
text = input()
text = text.rstrip()
quantity = text.count(' ') + 1

print('Количество слов:', quantity)

