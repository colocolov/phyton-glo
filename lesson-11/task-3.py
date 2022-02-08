print('Введите IP-адрес:')
ip = input()

adr = ip.split('.')
er = 0

for i in range(len(adr)):
    if int(adr[i]) > 255:
        er = 1
        break
if er == 0:
    print('YES')
else:
    print('NO')