chislo = int(input('Введите любое число: '))
reverse = 0
last_digit = 0

while chislo > 0:
    last_digit = chislo % 10
    reverse = reverse * 10 + last_digit
    chislo //= 10


print('Развернём число и получим:', reverse)