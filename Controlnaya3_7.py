#Задача 7. Поездка по кругу

v = int(input('Введите скорость: '))
t = int(input('Введите время в часах: '))
s = v*t
count_lap = s//115
if s<115:
    print('Вася остановился на',s,'километре.')
elif s>=115:
    res = s - count_lap*115
    print('Вася остановился на',res,'километре.')


