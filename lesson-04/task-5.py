print('Введите количество секунд:')
seconds = int(input())
hours = seconds // 3600
min = (seconds - hours * 3600 ) // 60
sec = (seconds - min * 60) % 100
print(seconds, 'секунд - это', hours, 'час', min, 'минут', sec, 'сек')