import requests


def get_exchange_rate(from_currency, to_currency):

    print("Currency tool called:", from_currency, "->", to_currency)

    try:

        url = f"https://open.er-api.com/v6/latest/{from_currency.upper()}"

        response = requests.get(url)

        data = response.json()

        if data["result"] != "success":
            return "Invalid currency code."

        rates = data["rates"]

        if to_currency.upper() not in rates:
            return "Target currency not found."

        rate = rates[to_currency.upper()]

        return f"""

Exchange Rate

From:
{from_currency.upper()}

To:
{to_currency.upper()}

Rate:
1 {from_currency.upper()} = {rate} {to_currency.upper()}

"""

    except Exception as e:

        return str(e)


def convert_currency(amount, from_currency, to_currency):

    print("Currency Conversion Tool Called")

    try:

        url = f"https://open.er-api.com/v6/latest/{from_currency.upper()}"

        response = requests.get(url)

        data = response.json()

        if data["result"] != "success":
            return "Invalid currency code."

        rates = data["rates"]

        if to_currency.upper() not in rates:
            return "Target currency not found."

        rate = rates[to_currency.upper()]

        converted = amount * rate

        return f"""

Currency Conversion

Amount:
{amount} {from_currency.upper()}

Converted Amount:
{converted:.2f} {to_currency.upper()}

Exchange Rate:
1 {from_currency.upper()} = {rate} {to_currency.upper()}

"""

    except Exception as e:

        return str(e)