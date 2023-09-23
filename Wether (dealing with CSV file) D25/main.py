# # This line opens the file "weather_data.csv" in read mode.
# with open("weather_data.csv") as data:
#
# # This line creates a list of lines in the file, stripping any whitespace from the end of each line.
# lines = [line.strip() for line in data.readlines()]
#
# # This line prints the list of lines.
# print(lines)
#
# # This line imports the csv module.
# import csv
#
# # This line opens the file "weather_data.csv" in read mode and creates a csv reader object.
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#
# # This line creates an empty list to store the temperatures.
# temperature = []
#
# # This loop iterates over the rows in the csv file.
# for row in data:
#
# # This condition checks if the current row is not the header row.
#     if row[1] != "temp":
#
# # This line appends the temperature from the current row to the temperature list.
#         temperature.append(int(row[1]))
#
# # This line prints the temperature list.
# print(temperature)

# This line imports the pandas module.
import pandas

# This line reads the "weather_data.csv" file into a pandas DataFrame.
data = pandas.read_csv("weather_data.csv")

# This line creates a list of the temperatures in the DataFrame.
data_temp = data["temp"].to_list()

# This line calculates the average temperature.
average = sum(data_temp) / len(data_temp)

# This line prints the average temperature.
print(f"the average is {average}")

# This line finds the maximum temperature in the DataFrame.
maximum = data.temp.max()

# This line prints the maximum temperature.
print(f"the maximum value is {max}")

# This line finds all rows in the DataFrame where the temperature is equal to the maximum temperature.
data[data.temp == maximum]

# This line creates a DataFrame of all rows in the DataFrame where the day is equal to "Monday".
monday = data[data.day == "Monday"]

# This line converts the temperatures in the DataFrame to Fahrenheit and prints the results.
print(f"monday tem in Fahrenheit is {monday.temp * 9 / 5 + 32}")
