import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data safely
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "sales.csv")

df = pd.read_csv(DATA_PATH)

# Convert date column
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

# Total sales by product
product_sales = df.groupby('product')['sales_amount'].sum()
print("Sales by Product:\n", product_sales)

# Monthly sales trend
monthly_sales = df.groupby('month')['sales_amount'].sum()

# Plot monthly sales
plt.figure()
monthly_sales.plot(kind='bar')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
