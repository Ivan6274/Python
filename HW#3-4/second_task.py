#Задача №2
#Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#   1. На вход обменнику вводишь количество денег int.
#    2. На выходе в консоль выводится отввет в таком виде:
#                "Ты ввёл int (Валюта)"
#               "Конвертированная сумма в USD = int"
#                "Конвертированная сумма в EUR = int"
#                "Конвертированная сумма в CHF = int"
#                "Конвертированная сумма в GBR = int"
#                "Конвертированная сумма в CNY = int"
#    3. Валюту пользователя определите сами.
usd, eur, chf, gbr, cny = 73.35, 86.85, 65.75, 102.35, 59.53
rub_money = int(input("please, input amount of rubles for exchange "))
print("You input", rub_money, "rubles")
print("Finally sum of USD after exchange =", round(rub_money/usd, 2))
print("Finally sum of EUR after exchange =", round(rub_money/eur, 2))
print("Finally sum of CHF after exchange =", round(rub_money/chf, 2))
print("Finally sum of GBR after exchange =", round(rub_money/gbr, 2))
print("Finally sum of CNY after exchange =", round(rub_money/cny, 2))