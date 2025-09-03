# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# 1. Using NumPy Array for Mean Calculation
array = np.arange(1, 11)  # Creates an array from 1 to 10
mean_calculation = np.mean(array)
print("NumPy Array:", array)
print("Mean of the array:", mean_calculation)

# 2. Load a small dataset and display summary statistics
# We'll use a built-in dataset from seaborn (if installed) or just create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 28],
    'Salary': [50000, 60000, 70000, 80000, 62000]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:\n", df)
print("\nSummary Statistics:\n", df.describe())

# 3. Fetch data from a public API using requests
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
if response.status_code == 200:
    bitcoin_data = response.json()
    price_usd = bitcoin_data['bpi']['USD']['rate']
    print("\nCurrent Bitcoin Price in USD:", price_usd)
else:
    print("\nFailed to fetch data from API")

# 4. Plot a simple line graph using matplotlib
x = [1, 2, 3, 4, 5]
y = [10, 12, 15, 13, 17]
plt.plot(x, y, marker='o', linestyle='-', color='blue')
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
