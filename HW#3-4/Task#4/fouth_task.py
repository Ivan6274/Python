# Задача №4
# Обменник. Скрипт запускается в консоли и работает постоянно. Остановится нажатием ctrl+c.
#     1. Скрипт сначала выводит "Выберите валюту из ['USD','EUR','CHF','GBP','CNY']"
#     2. Пользователь вводит один из 5 вариантов ['USD','EUR','CHF','GBP','CNY']
#     3. Потом Скрипт выводит "Введите сумму"
#     4. Пользователь вводит сумму int
#     5. Скрипт выводит:
#             "Вы ввели сумму int и валюту "Валюта" "
#             "конвертированная сумма в "Валюта" = int"
#     6. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     7. После сообщеня об ошибке, скрипт должен автоматом вернуться к шагу 1.

currency = {'USD': 72.35, 'EUR': 86.75, 'CHF': 65.2, 'GBP': 103.88, 'CNY': 34.55}
while True:
    name_of_the_currency = input("Select a currency from ['USD','EUR','CHF','GBP','CNY'] ")
    if name_of_the_currency in currency:

        while True:
            rub_money = input("Please,enter the amount in rubles to exchange ")

            if rub_money == "":
                print("You didn't enter anything")
                continue
            if rub_money.lstrip("-").isdigit():
                if int(rub_money) > 0:
                    result = round((int(rub_money) / int(currency.get(name_of_the_currency))), 2)
                    print("You have entered the amount", rub_money, "and the currency", name_of_the_currency)
                    print("The converted amount in", name_of_the_currency, "=", result)

                    break
                else:
                    print("Please, enter the positive number")
                    continue
            else:
                print("You didn't enter a number, please enter a number")
                continue
    else:
        print("Incorrect entry of the currency name")
        continue
