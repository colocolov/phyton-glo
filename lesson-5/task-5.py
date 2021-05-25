print('Введите количество задач:')
tasks = int(input())
print('Сколько задач вы сделаете за день:')
quantity = int(input())

days = tasks // quantity
rest = tasks % quantity

#print(int(days))
#print(rest)

if rest != 0:
    days += 1
print('Вам надо', days, 'дней')
