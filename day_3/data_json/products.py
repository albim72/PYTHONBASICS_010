import json
import pandas as pd

# Load JSON file
with open("products.json", "r") as f:
    data = json.load(f)

#Create a Pandas DataFrame
df = pd.DataFrame(data["products"])
print("Product DataFrame:")
print(df)

# Calculate average price
avg_price = df["price"].mean()
print("\nAverage product price:", round(avg_price, 2))

# Show only available products
print("\nProducts in stock:")
print(df[df["in_stock"] == True])
