import math

print('Введите трех значния: рубли, копейки, кол-во:')
rubs = int(input())
coints = float(input()) / 100
quantity = int(input())
price = rubs + coints
total = price * quantity
print('За', quantity, 'мяча нужно зплатить', int(total), 'рублей', math.ceil(total % 1), 'копеек')
