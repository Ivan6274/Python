
def valid_amount_result(amount, name_of_the_currency):
    currency = {'USD': 72.35, 'EUR': 86.75, 'CHF': 65.2, 'GBP': 103.88, 'CNY': 34.55}
    result = round((int(amount) / int(currency.get(name_of_the_currency))), 2)

    return print("You have entered the amount", amount, "and the currency", name_of_the_currency,
                 "\nThe converted amount in", name_of_the_currency, "=", result)
