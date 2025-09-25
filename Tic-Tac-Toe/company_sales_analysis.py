import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load data
df = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Flexisaf Internship\DS Internship projects\Tic-Tac-Toe\company_sales_data.csv")
print(df.head())

#Exercise 1: Line plot for total profit
plt.figure(figsize=(8,5))
plt.plot(df['month_number'], df['total_profit'], marker='o', color='b', linewidth=2)
plt.title("Company Profit per Month")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.grid(True)
plt.show()


# Exercise 2: Subplots for Bathing Soap and Facewash
plt.figure(figsize=(10,6))

# Bathing Soap subplot
plt.subplot(2,1,1)
plt.plot(df['month_number'], df['bathingsoap'], marker='o', color='g', linewidth=2)
plt.title("Bathing Soap Sales Data")
plt.xlabel("Month Number")
plt.ylabel("Units Sold")
plt.grid(True)


# Facewash subplot
plt.subplot(2,1,2)
plt.plot(df['month_number'], df['facewash'], marker='o', color='m', linewidth=2)
plt.title("Facewash Sales Data")
plt.xlabel("Month Number")
plt.ylabel("Units Sold")
plt.grid(True)

plt.tight_layout()
plt.show()