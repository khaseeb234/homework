# age = int(input("Ваш возраст: "))
# if age >=0 and age <=11:
# print("Ребенок")
# elif age >=12 and age <=18:
# print("Подросток")
# elif age >=19 and age <=60:
# print("Взрослый")
# else:
# print("пенсионер")

# num = int(input("Введите число от 0 до 9: "))



# if num == 0:
#     print(")")
# elif num == 1:
#     print("!")
# elif num == 2:
#     print("!@")
# elif num == 3:
#     print("#")
# elif num == 4:
#     print("$")
# elif num == 5:
#     print("%")
# elif num == 6:
#     print("^")
# elif num == 7:
#     print("&")
# elif num == 8:
#     print("*")
# elif num == 9:
#     print("(")
# else:
#     print("ошибка! Число можно ввести только от 0 до 9")





# num = int(input("Введите трехзначное число: "))

# if num <=100 or num > 999:
#     print("Число должно быть трехзначным")
# else:
#     a = num //100
#     b = (num %100)//10
#     c = num %10
#     if a == b or b == c or c == a:
#         print("Числа одиноковые")
#     else:
#         print("числа разные")



# year = int(input("год: "))

# if (year %4 == 0 and year %100 !=0) or (year %400 == 0):
#     print("Год високосный")
# else:
#     print("Год не високосный")




# discharge = int(input("Введите пятиразрядное число: "))

# if discharge <10000 or discharge >=99999:
#     print("Число должно быть пятиразрядным")
# else:
#     num1 = discharge//10000
#     num2 = (discharge//1000)%10
#     num3 = (discharge//100)%10
#     num4 = (discharge//10)%10
#     num5 = discharge %10
#     if num1 == num5 and num2 == num4:
#         print("Число является палиндромом")
#     else:
#         print("число не является палиндромом")




# user_usd = float(input("Введите сумму в доллорах(USD): "))

# if user_usd <=0:
#     print("Ошибка: сумма должна быть положительной")
# else:
#     convert = input("Выберите валюту в которую хотите конвертировать (EUR/UAN/AZN)")
#     if convert == "EUR":
#         eur = 0.87
#         result = user_usd * eur
#         print(f"Валюта было успешно конвертирована: {result} Евро")
#     elif convert == "UAN":
#         uan = 6.77
#         result = user_usd * uan
#         print(f"Конвертация прошла успешно: {result} Юань")
#     elif convert == "AZN":
#         azn = 1.70
#         result = user_usd * azn
#         print(f"Конвертация прошла успешно: {resul} азер")
#     else:
#         print("Ошибка: допустимо только из предложенных EUR/UAN/AZN")




# user_coupon = float(input("Сумма покупки в рублях: "))
# if user_coupon <= 0:
#     print("Ошибка: сумма должна быть положительной")
# else:
#     if user_coupon >=200 and user_coupon < 300:
#         price = user_coupon * 0.03
#         result = user_coupon - price
#         print(f"Скидка применена: {result}")
#     elif user_coupon >=300 and user_coupon < 500:
#         price = user_coupon * 0.05
#         result = user_coupon - price
#         print(f"Скидка применена: {result}")
#     elif user_coupon >= 500:
#         price = user_coupon * 0.07
#         result = user_coupon - price
#         print(f"Скидка применена: {result}")
#     else:
#         print(f"Итоговая сумма без скидки: {user_coupon}")

user = int(input("Введите число: "))
print(user)