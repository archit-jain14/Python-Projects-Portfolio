import requests


def get_exchange_rate(from_currency, to_currency):
    # Free currency rate API (no API key required)
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        rates = data.get("rates", {})
        if to_currency.upper() in rates:
            return rates[to_currency.upper()]
        else:
            print(f"❌ Error: Currency '{to_currency}' not found.")
            return None

    except requests.exceptions.RequestException:
        print(
            "❌ Network Error: Unable to fetch exchange rates. Check your internet connection."
        )
        return None


def main():
    print("=" * 45)
    print("💱 Welcome to Real-Time Currency Converter! 💱")
    print("=" * 45)

    try:
        amount = float(input("Enter amount to convert: "))
        from_curr = (
            input("From Currency (e.g., USD, INR, EUR): ").strip().upper()
        )
        to_curr = input("To Currency (e.g., INR, USD, EUR): ").strip().upper()

        if amount <= 0:
            print("⚠️ Amount must be greater than 0.")
            return

        print("\n⏳ Fetching live exchange rates...")
        rate = get_exchange_rate(from_curr, to_curr)

        if rate:
            converted_amount = amount * rate
            print("\n" + "✨" * 20)
            print(
                f"💵 {amount:.2f} {from_curr} = {converted_amount:.2f} {to_curr}"
            )
            print(f"📊 Live Exchange Rate: 1 {from_curr} = {rate} {to_curr}")
            print("✨" * 20)

    except ValueError:
        print("❌ Invalid input! Please enter a numeric value for amount.")


if __name__ == "__main__":
    main()