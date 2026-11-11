
import csv

total_revenue = 0
total_transactions = 0
product_sales = {}

# Read CSV file
with open("data/sales.csv", "r", encoding="utf-8-sig", newline="") as file:

    reader = csv.DictReader(file)

    # Clean column names
    reader.fieldnames = [
        name.strip().replace("\ufeff", "") for name in reader.fieldnames
    ]

    for row in reader:
        product = row["Product"].strip()
        quantity = int(row["Quantity"])
        price = float(row["Price"])

        revenue = quantity * price

        total_revenue += revenue
        total_transactions += 1

        product_sales[product] = product_sales.get(product, 0) + revenue

if total_transactions == 0:
    print("No sales records found.")
else:
    best_product = max(product_sales, key=product_sales.get)

    print("\n================================")
    print("       MINI SALES ANALYZER")
    print("================================")

    print(f"Total Transactions : {total_transactions}")
    print(f"Total Revenue      : ₹{total_revenue:,.2f}")
    print(f"Average Sale       : ₹{total_revenue / total_transactions:,.2f}")

    print("\n----- PRODUCT PERFORMANCE -----")

    for product, revenue in sorted(
        product_sales.items(),
        key=lambda item: item[1],
        reverse=True
    ):
        print(f"{product:<15} ₹{revenue:,.2f}")

    print("\n----- BEST PERFORMER -----")
    print(f"Top Product: {best_product}")
    print(f"Revenue: ₹{product_sales[best_product]:,.2f}")
