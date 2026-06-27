#1 задача
# UserName = input("Ваша имя: ")
# UserAge = int(input("Ваш возраст: "))
# print(f"Имя: {UserName}\nВозраст: {UserAge}")

#2 задача
# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# c = int(input("Введите число: "))
# d = int(input("Введите число: "))
# maximum = a
# if b > maximum:
#     maximum = b
# if c > maximum:
#     maximum = c
# if d > maximum:
#     maximum = d
# print(f"Максимальное число: {maximum}")

#3 задача
# Number = int(input("Выберите фигуру: 1 - квадрат. 2 - прямоугольник: "))
# if Number == 1:
#     a = int(input("Введите сторону квадрата: "))
#     area = a * a
#     print(f"Площадь квадрата: {area}")
# elif Number == 2:
#     a = int(input("Введите длину прямоугольника: "))
#     b = int(input("Введите ширину прямоугольника: "))
#     area = a * b
#     print(f"Площадь прямоугольника: {area}")

#4 задача
# a = int(input("Введите целое число: "))
# b = int(input("Введите целое число: "))
# if a <= b:
#     for i in range(a, b + 1):
#         print(i)
# else:
#     for i in range(a, b -1, -1):
#         print(i)

#5 задача
# summa = 0
# product = 1
# while True:
#     x = int(input("Введите число: "))
#     if x == 0:
#         break
#     else:
#         summa += x
#         product *= x
# print(f"Сумма: {summa}\nПроизведение: {product}")

#6 задача
# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# if a > b:
#     start = a
#     end = b
#     print(f"{start}\n{end}")
# else:
#     start = b
#     end = a
#     print(f"{start}\n{end}")
# print("----" * 5)
# for i in range(start, end - 1, -1):
#     if i % 3 == 0:
#         print(i)

#7 задача
# for i in range(1,11):
#     for j in range(1,11):
#         print(i * j, end="\t")
#     print()

#8 задача
# n = int(input("Введите число: "))
# if n <= 0:
#     print("Введено некорректное число")
# elif n > 0:
#     first = int(input("Введите число: "))
#     max_num = first
#     min_num = first
#     for i in range(1, n):
#         x = int(input("Введите число: "))
#         if x > max_num:
#             max_num = x
#         if x < min_num:
#             min_num = x
#     print(f"Максимальное число: {max_num}\nминимальное число: {min_num}")

#9 задача
# n = int(input("Введите число: "))
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end=" ")
#     for k in range(2 * i + 1):
#         print("*", end=" ")
#     print()

import random

target = int(input("До скольки побед играем? "))
pc_wins = 0
pl_wins = 0
choice = 0
while True:
    while True:
        pc = random.randint(0,1)
        guess = input("Введи чет или 'нечет' ")
        if guess == "чет":
            choice = 0
        else:
            choice = 1

        if choice == pc:
            print("Угадал!")
            pl_wins += 1
        else:
            print("Не угадал. Победа компьютера")
            pc_wins += 1

        if pl_wins == target:
            print(f"Игрок выйграл со счетом: {pl_wins}:{pc_wins}")
            break
        elif pc_wins == target:
            print(f"Компьютер выйграл со счетом: {pc_wins}:{pl_wins}")
            break
    again = input("Хотите сыграть еще раз? (да/нет): ")
    if again != "да":
        break