print('Введите числа:')
numbers = input()
couple = 0

num_spl = numbers.split(' ')
print(num_spl)

for i in range(len(numbers)):
    if numbers[i] in numbers:
        print(numbers[i])
        couple += 1


print(couple)
