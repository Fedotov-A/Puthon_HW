# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. В последующих  строках записаны N
# целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

# import random

# list_1 = []
# count = 0
# num = int(input("Введите размер массива "))
# x_num = int(input("Введите число для поиска "))
# for i in range(num):
#     list_1.append(random.randint(1, num))
# print(list_1)
# for i in range(len(list_1)):
#     if x_num == list_1[i]:
#         count += 1
# print(f"Число {x_num} повторилось {count} раз")


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. В последующих  строках записаны
# N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

# list_1 = []
# list_2 = []
# num = int(input("Введите размер массива "))
# x_num = int(input("Введите желаемое число "))
# min_num = num
# for i in range(num):
#     list_1.append(random.randint(1, num))
# print(list_1)

# for i in range(len(list_1)):
#     list_2.append(abs(x_num - list_1[i]))
# print(list_2)

# for i in range(len(list_2)):
#     if list_2[i] < min_num:
#         min_num = list_2[i]
# print(f"Число {min_num + x_num} самое близкое по значению")
