import pandas as pd

df = pd.read_csv("../data/logistics_simulated_clean.csv")
df["on_time"] = df["delivery_hours"] <= 24  # illustrative threshold only

print("Average delivery hours:", df["delivery_hours"].mean())
print("Average cost (INR):", df["transport_cost_inr"].mean())
print("Illustrative on-time rate (%):", 100 * df["on_time"].mean())
print(df.groupby("warehouse")["delivery_hours"].median())
