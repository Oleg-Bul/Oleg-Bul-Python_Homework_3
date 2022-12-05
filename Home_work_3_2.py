# 2'. Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


list1 = [2, 3, 4, 5, 6]
SumList = []
j = -1
for i in range(len(list1)):
    if i < (len(list1)/2):
        SumList.append(list1[i]*list1[j])
        j += -1
print(SumList)

# Решение от преподователя


def pair_multi(nums: list[int]) -> int:
    """Возвращает список произведений пар элементов"""
    pairs = []
    iterations = int(round((len(nums)+1)/2))
    print(iterations)
    for i in range(iterations):
        pairs.append(nums[i]*nums[-1-i])
    return pairs


nums = [2, 3, 5, 6, 3, 5, 6]
print(pair_multi(nums))
