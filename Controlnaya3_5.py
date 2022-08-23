# Задача 5. Часы

minute = int(input('Введите количество минут: '))

hour = minute // 60
min = minute % 60

print(minute,'минуты - это',hour,'часов и',min,'минуты')