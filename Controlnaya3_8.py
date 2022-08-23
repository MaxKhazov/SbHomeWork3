# Задача 8. «Режем» число на части
chislo = int(input('Введите любое четырехзначное число: '))
print(chislo//1000)
print(chislo%1000//100)
print(chislo%100//10)
print(chislo%10)