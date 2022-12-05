# 5'. Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов. (Дополнительное)
# *Пример:*
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


fib1 = fib2 = 1
n = int(input('Введите номер элемента фибонначи : '))
listFibon = [0]
listFibon.append(fib1)
listFibon.append(fib2)
listFibon.insert(0, (fib2))
listFibon.insert(0, (fib2*-1))
for j in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    listFibon.append(fib2)
    if j % 2 == 0:
        listFibon.insert(0, (fib2))
    else:
        listFibon.insert(0, (fib2*-1))
print('Список чисел фибоначи, для числа ', n, ': ', listFibon)
