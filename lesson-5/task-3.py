print('Введите 6-ное число:')
number = int(input())

digit_one = number // 100000
digit_two = number % 100000 // 10000
digit_three = number % 10000 // 1000

digit_four = number % 1000 // 100
digit_five = number % 100 // 10
digit_six = number % 10

#print(digit_one)
#print(digit_two)
#print(digit_three)
#print(digit_four)
#print(digit_five)
#print(digit_six)

sum_1 = digit_one + digit_two + digit_three
sum_2 = digit_four + digit_five + digit_six

if sum_1 == sum_2:
    print('Билет', number, 'счастливый')
else:
    print('Билет', number, 'НЕсчастливый')
