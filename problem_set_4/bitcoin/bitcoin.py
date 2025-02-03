import sys
import requests


def main():
    bitcoin_quantity = get_bitcoin_quantity()
    bitcoin_price = fetch_bitcoin_price()
    total_cost = calculate_total_cost(bitcoin_quantity, bitcoin_price)
    print(f"${total_cost:,.4f}")


def get_bitcoin_quantity():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
        return n
    except ValueError:
        sys.exit("Command-line argument is not a number")


def fetch_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Failed to retrieve data")


def calculate_total_cost(quantity, price_per_bitcoin):
    return quantity * price_per_bitcoin


if __name__ == "__main__":
    main()
