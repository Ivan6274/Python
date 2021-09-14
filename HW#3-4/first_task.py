#Задача №1
#Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#    1. На вход обменнику вводишь количество денег int.
#    2. На выходе в консоль выводится отввет в таком виде:
#                "Ты ввёл int (Валюта)"
#                "конвертированная сумма в USD = int" Лучше сделать float!!!
#   3. Валюту пользователя определите сами
rub_money = int(input("please, input amount of rubles for exchange "))
usd = float(input("please, input current exchange rate of USD "))
print("You input", rub_money, "rubles")
print("Finally sum of USD after exchange", round(rub_money/usd, 2), "$")
