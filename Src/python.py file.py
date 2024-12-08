import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
healthy_food_data = pd.read_csv('Indian_Healthy_Food_Calories.csv')
fast_food_data = pd.read_csv('Indian_Fast_Food_Calories.csv')

# Number of items to display
num_items_to_display = 21

# Preparing the data
healthy_items = healthy_food_data.head(num_items_to_display)
fast_food_items = fast_food_data.head(num_items_to_display)

# Plot for Healthy Food
plt.figure(figsize=(10, 6))
plt.bar(healthy_items['Food Item'], healthy_items['Calories (Approx)'], 
        color='green', alpha=0.7)
plt.title('Calories in Healthy Food', fontsize=14)
plt.xlabel('Food Item', fontsize=12)
plt.ylabel('Calories (Approx)', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.show()

# Plot for Fast Food
plt.figure(figsize=(10, 6))
plt.bar(fast_food_items['Food Item'], fast_food_items['Calories (Approx)'], 
        color='red', alpha=0.7)
plt.title('Calories in Fast Food', fontsize=14)
plt.xlabel('Food Item', fontsize=12)
plt.ylabel('Calories (Approx)', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.show()