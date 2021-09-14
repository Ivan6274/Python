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
usd, eur, chf, gbr, cny = 73.35, 86.85, 65.75, 102.35, 59.53

while True:
    rub_money = input("please, input amount of rubles for exchange ")

    if rub_money == "":
        print("You input nothing, please, input amount of rubles for exchange ")
        continue
    if rub_money.lstrip("-").isdigit():
        if int(rub_money) > 0:
            print("You input", rub_money, "rubles")
            print("Finally sum of USD after exchange =", round(int(rub_money) / usd, 2))
            print("Finally sum of EUR after exchange =", round(int(rub_money) / eur, 2))
            print("Finally sum of CHF after exchange =", round(int(rub_money) / chf, 2))
            print("Finally sum of GBR after exchange =", round(int(rub_money) / gbr, 2))
            print("Finally sum of CNY after exchange =", round(int(rub_money) / cny, 2))
            break
        else:
            print("Please, input a positive number")
            continue
    else:
        print("You input not a number, please input a number")
        continue
