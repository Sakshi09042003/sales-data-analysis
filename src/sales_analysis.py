import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "sales.csv")
VISUAL_PATH = os.path.join(BASE_DIR, "visuals")

# Create visuals folder if not exists
os.makedirs(VISUAL_PATH, exist_ok=True)

df = pd.read_csv(DATA_PATH)
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

monthly_sales = df.groupby('month')['sales_amount'].sum()

plt.figure()
monthly_sales.plot(kind='bar')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()

# Save image
plt.savefig(os.path.join(VISUAL_PATH, "monthly_sales.png"))
plt.close()
