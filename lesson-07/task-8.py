print('Введите количество чисел, которые хотите ввести:')
quantity = int(input())

maximum = 0
minimum = quantity

for i in range(quantity):
    number = int(input())
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number
    
print('Минимум равен', minimum)
print('Максимум равен', maximum)
