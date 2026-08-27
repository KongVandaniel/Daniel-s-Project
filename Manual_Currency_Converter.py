# Currency Converter (Manual)

from Daniel_Project.Projects_D.utils import typewriter_print, get_safe_input, colorize, BOLD, RED

# CURRENCY
currencies = {
    "USD": {
        "name": "US Dollar",
        "symbol": "$"
    },
    "KHR": {
        "name": "Cambodian Riel",
        "symbol": "៛"
    },
    "EUR": {
        "name": "Euro",
        "symbol": "€"
    },
    "GBP": {
        "name": "British Pound",
        "symbol": "£"
    },
    "JPY": {
        "name": "Japanese Yen",
        "symbol": "¥"
    },
    "CNY": {
        "name": "Chinese Yuan",
        "symbol": "¥"
    },
    "KRW": {
        "name": "South Korean Won",
        "symbol": "₩"
    }
}

# EXCHANGE RATE
rates = {
    "USD": {
        "USD": 1,
        "KHR": 4000,
        "EUR": 0.86,
        "GBP": 0.75,
        "JPY": 147,
        "CNY": 7.18,
        "KRW": 1390
    }
}

# CHOOSE CURRENCY
def choose_currency(message):
            while True:
                print()
                typewriter_print(message)
                print()
                typewriter_print(f"1. {'USD - US Dollar':<25} ($)")
                typewriter_print(f"2. {'KHR - Cambodian Riel':<25} (៛)")
                typewriter_print(f"3. {'EUR - Euro':<25} (€)")
                typewriter_print(f"4. {'GBP - British Pound':<25} (£)")
                typewriter_print(f"5. {'JPY - Japanese Yen':<25} (¥)")
                typewriter_print(f"6. {'CNY - Chinese Yuan':<25} (¥)")
                typewriter_print(f"7. {'KRW - South Korean Won':<25} (₩)")
                print()
                choice = input("Select currency: ")

                if choice == "1":
                    return "USD"
                elif choice == "2":
                    return "KHR"
                elif choice == "3":
                    return "EUR"
                elif choice == "4":
                    return "GBP"
                elif choice == "5":
                    return "JPY"
                elif choice == "6":
                    return "CNY"
                elif choice == "7":
                    return "KRW"
                else:
                    typewriter_print(
                        colorize(
                            "⚠️ Invalid currency choice.",
                            RED
                        )
                    )

def main_menu():
    while True:
        print()
        typewriter_print("===== Currency Converter =====")
        
        # Choose FROM Currency
        from_currency = choose_currency("===== From Currency =====")
        print()
        # Choose TO Currency
        to_currency = choose_currency("===== To Currency =====")

        print()

        from_name = currencies[from_currency]["name"]
        from_symbol = currencies[from_currency]["symbol"]

        to_name = currencies[to_currency]["name"]
        to_symbol = currencies[to_currency]["symbol"]

        print()
        
        # Enter Amount
        while True:
            try: 
                amount = float(input(f"Enter Amount in {from_currency} ({from_symbol}): "))
                if amount < 0:
                     raise ValueError("Amount cannot be negative.")
                break
            except ValueError as err:
                 typewriter_print(colorize(f"⚠️ {err}",RED))

        # Calculate
        if from_currency == "USD":
            rate = rates["USD"][to_currency]
            converted_amount = amount * rate
        else:
            # Convert FROM currency → USD first
            usd_amount = (amount / rates ["USD"][from_currency])
            # Then USD → TO currency
            rate = rates["USD"][to_currency]
            converted_amount = usd_amount * rate

        # Result
        from_name = currencies[from_currency]["name"]
        from_symbol = currencies[from_currency]["symbol"]

        to_name = currencies[to_currency]["name"]
        to_symbol = currencies[to_currency]["symbol"]

        print()

        typewriter_print(
            f"From: {from_name:<15} {from_currency} ({from_symbol})"
        )

        typewriter_print(
            f"To:   {to_name:<15} {to_currency} ({to_symbol})"
        )

        print()
        print()

        typewriter_print("===== Conversion Result =====")

        print()

        typewriter_print(f"{from_name} -> {to_name}")

        print()

        typewriter_print(
                f"{'From:':<15} "
                f"{amount:,.2f} {from_currency} ({from_symbol})"
            )

        typewriter_print(
                f"{'Converted To:':<15} "
                f"{converted_amount:,.2f} {to_currency} ({to_symbol})"
            )

        print()
        print()
        again = input("Convert another amount? (Yes/No): ")
        if again.lower() == "no":
            print()
            typewriter_print("===== Thank You For Choosing Our Converter! =====")
            print()
            break

main_menu()