print('Введите число или ноль для завершения ввода:')
number = int(input())

total = 0
quantity = 0

while number != 0:
    total = total + number
    quantity += 1
    number = int(input())
middle = total / quantity

print(int(middle))
