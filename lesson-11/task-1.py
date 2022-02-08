print('Введите кол-во слов:')
quantity = int(input())

words = []
print('Введите', quantity, 'слов:')
for i in range(0, quantity, 1):
    word = input()
    words.append(word)

print('Введите поисковый запрос:')
search = input().lower()

print('Результат:')
for value in words:
    value_l = value.lower()
    if search in value_l:
        print(value)