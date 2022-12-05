# 3. Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19 (максимальное значение у числа 1.2 ,
#  минимальное у 10.01)

list1 = [1.1, 1.2, 3.1, 5, 10.01]
list2 = []

for i in range(len(list1)):
    list2.append(round(float((list1[i]) - int(list1[i])), 3))

print(list1)
print(list2)
a = 0
b = 1
for i in range(len(list2)):
    if list2[i] > a:
        a = float(list2[i])
    if list2[i] < a:
        b = float(list2[i])
sum = (a - b)
print('Разница между min и max значений дробной части элементов:', float(sum))

# Решение от преподователя


def separate_fraction(num: float) -> float:
    """Отделяет дробную часть от целой"""
    list_num = str(num).split('.')  # ['1','11']
    return float('0.'+list_num[1])  # 0.11


def max_vs_min_fraction(num_list: list[float]) -> float:
    """Возвращает разницу между максимальныи и минимальным дробным значением
     списка"""
    new_list = [separate_fraction(i) for i in num_list if int(i) != float(i)]
    print(new_list)
    return max(new_list) - min(new_list)


example = [1.1, 1.2, 3.1, 5, 10.001]
print(max_vs_min_fraction(example))

