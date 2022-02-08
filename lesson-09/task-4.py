print('Введите число:')
number = int(input())

for i in range(1, number + 1):
    if i > 1 and i < 9 or i > 127 and i < 257 or i > 1023 and i < 2049:
        continue
    print(i)
