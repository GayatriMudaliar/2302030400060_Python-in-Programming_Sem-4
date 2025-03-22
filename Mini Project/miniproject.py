import numpy as np
import matplotlib.pyplot as plt

# 1️⃣ Create a random dataset
data = np.random.randint(1, 100, size=(10, 5))  # 10 rows, 5 columns
print("Generated Data:\n", data)

# 2️⃣ Calculate basic statistics
mean_values = np.mean(data, axis=0)
median_values = np.median(data, axis=0)
std_dev_values = np.std(data, axis=0)

print("\nMean Values:", mean_values)
print("Median Values:", median_values)
print("Standard Deviation:", std_dev_values)

# 3️⃣ Perform matrix operations
transpose_data = np.transpose(data)
dot_product = np.dot(transpose_data, data)
print("\nDot Product of Matrix:\n", dot_product)

# 4️⃣ Visualize the data using Matplotlib
plt.figure(figsize=(8, 5))

# Bar plot for mean values
plt.bar(range(len(mean_values)), mean_values, color='blue', label='Mean')

# Scatter plot for standard deviation
plt.scatter(range(len(std_dev_values)), std_dev_values, color='red', label='Std Dev')

plt.xlabel("Column Index")
plt.ylabel("Values")
plt.title("NumPy Data Analysis")
plt.legend()
plt.show()
