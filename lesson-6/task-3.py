print('Введите 1-ю статью:')
text_one = input()
length_one = len(text_one)
print('Введите 2-ю статью:')
text_two = input()
length_two = len(text_two)
print('Введите 3-ю статью:')
text_three = input()
length_three = len(text_three)

if length_one > length_two:
    if length_one > length_three:
        print(text_one)
    else:
        print(text_three)
else:
    if length_two > length_three:
        print(text_two)
    else:
        print(text_three)
    