import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

# Display data
print(df.head())

# Total sales
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

# Average Order Value
average_order = df["Sales"].mean()
print("Average Order Value:", average_order)

# Top products
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("Top Products:")
print(top_products)

# Category-wise sales
category_sales = df.groupby("Category")["Sales"].sum()
print("Category-wise Sales:")
print(category_sales)

# Region-wise sales
region_sales = df.groupby("Region")["Sales"].sum()
print("Region-wise Sales:")
print(region_sales)