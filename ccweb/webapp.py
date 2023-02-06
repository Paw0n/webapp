def currency_calculator(amount, from_currency, to_currency):
    exchange_rates = {
        'USD': 1.0,
        'RUB': 10.0,
        'NGN': 5.76,
        'INR': 72.93
    }

    from_rate = exchange_rates[from_currency]
    to_rate = exchange_rates[to_currency]
    return amount * (to_rate / from_rate)

amount = float(input("Enter amount: "))
from_currency = input("Enter from currency: ")
to_currency = input("Enter to currency: ")

result = currency_calculator(amount, from_currency, to_currency)
print("%.2f %s is equivalent to %.2f %s" % (amount, from_currency, result, to_currency))

