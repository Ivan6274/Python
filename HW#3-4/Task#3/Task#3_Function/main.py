# Задача №3
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#                 "конвертированная сумма в EUR = int"
#                 "конвертированная сумма в CHF = int"
#                 "конвертированная сумма в GBP = int"
#                 "конвертированная сумма в CNY = int"
#
#     3. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
from result_of_exchage import resul_of_exchange
currency = {'USD': 72.35, 'EUR': 86.75, 'CHF': 65.2, 'GBP': 103.88, 'CNY': 34.55}

while True:
    rub_money = input("please, input amount of rubles for exchange ")

    if rub_money == "":
        print("You input nothing, please, input amount of rubles for exchange ")
        continue
    if rub_money.lstrip("-").isdigit():
        if int(rub_money) > 0:
            print("You input", rub_money, "rubles")
            for key, value in currency.items():
                resul_of_exchange(key, value, rub_money)
            break
        else:
            print("Please, input a positive number")
            continue
    else:
        print("You input not a number, please input a number")
        continue
