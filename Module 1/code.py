# Currency Converter - Module 1
# Basic converter using predefined exchange rates


# Exchange rates with USD as the base currency
exchange_rates = {
    "USD": 1.0,
    "INR": 83.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 149.0
}


def display_currencies():
    """Display all supported currencies."""
    print("\nAvailable Currencies:")
    
    for currency in exchange_rates:
        print("-", currency)


def get_currency(prompt):
    """Get and validate currency input from the user."""

    while True:
        currency = input(prompt).upper().strip()

        if currency in exchange_rates:
            return currency

        print("Invalid currency. Please choose from the available currencies.")


def get_amount():
    """Get and validate the amount from the user."""

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount > 0:
                return amount

            print("Amount must be greater than zero.")

        except ValueError:
            print("Invalid amount. Please enter a number.")


def convert_currency(amount, source_currency, target_currency):
    """Convert amount from source currency to target currency."""

    # Convert source currency to USD
    amount_in_usd = amount / exchange_rates[source_currency]

    # Convert USD to target currency
    converted_amount = amount_in_usd * exchange_rates[target_currency]

    return converted_amount


def main():
    """Main program function."""

    print("=" * 40)
    print("       CURRENCY CONVERTER")
    print("=" * 40)

    while True:

        display_currencies()

        source_currency = get_currency(
            "\nEnter source currency: "
        )

        target_currency = get_currency(
            "Enter target currency: "
        )

        amount = get_amount()

        converted_amount = convert_currency(
            amount,
            source_currency,
            target_currency
        )

        print("\n----------------------------------------")
        print(
            f"{amount:.2f} {source_currency} = "
            f"{converted_amount:.2f} {target_currency}"
        )
        print("----------------------------------------")

        choice = input(
            "\nDo you want to perform another conversion? (y/n): "
        ).lower().strip()

        if choice != "y":
            print("\nThank you for using Currency Converter!")
            break


# Start the program
if __name__ == "__main__":
    main()
