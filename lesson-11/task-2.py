print('Введите путь к файлу:')
path = input()

new_path = path.split('\\')

for i in range(len(new_path)):
    print(new_path[i])
