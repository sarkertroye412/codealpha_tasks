stock_prices = { 
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}

portfolio = {}
total_investment = 0

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable stocks:")

for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

print("\nEnter 'done' when you are finished.\n")

while True:
    stock_name = input("Enter stock symbol: ").upper()

    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("❌ Stock not available. Please choose from the list.\n")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        if quantity <= 0:
            print("Quantity must be greater than 0.\n")
            continue

    except ValueError:
        print("Please enter a valid number.\n")
        continue

    investment = stock_prices[stock_name] * quantity

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    total_investment += investment

    print(f"Added {quantity} shares of {stock_name}.")
    print(f"Investment value: ${investment}\n")


print("\n================================")
print("       YOUR PORTFOLIO")
print("================================")

if len(portfolio) == 0:
    print("No stocks were added.")

else:
    print("\nStock\tQuantity\tPrice\tValue")
    print("----------------------------------------")

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]
        value = price * quantity

        print(f"{stock}\t{quantity}\t\t${price}\t${value}")

    print("----------------------------------------")
    print(f"Total Investment: ${total_investment}")

with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("======================\n\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity

        file.write(
            f"{stock} | Quantity: {quantity} | "
            f"Price: ${price} | Value: ${value}\n"
        )

    file.write(f"\nTotal Investment: ${total_investment}")
print("\n✅ Portfolio has been saved to portfolio.txt")