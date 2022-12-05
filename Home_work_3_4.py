# 4. Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите число: '))
# print('Ваше число в двоичной системе: ', bin(int(number)))
numberB = ''
while number > 0:
    numberB = str(number % 2) + numberB
    number = number // 2
print('Ваше число в двоичной системе: ', numberB)
