import pandas as pd

# Read the Squirrel data CSV file
data = pd.read_csv("Central_Park_Squirrel_Data.csv")

# Extract the Squirrel fur color column
primary_fur = data["Primary Fur Color"]

# Count the number of each color
color_counts = primary_fur.value_counts()

# Create a new DataFrame with the color counts
df_color_counts = pd.DataFrame({'Squirrel Fur Color': color_counts.index, 'Count': color_counts.values})

# Save the new DataFrame to a CSV file
df_color_counts.to_csv('squirrel_fur_color.csv', index=True)
