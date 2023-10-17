# Import pandas and matplotlib libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file into a dataframe
df = pd.read_csv("nycflights.csv")


# Define a function to classify flights as late or not late based on departure and arrival delays
def late_or_not(row):
    if row["dep_delay"] > 0 or row["arr_delay"] > 0:
        return "Late"
    else:
        return "Not late"


# Apply the function to the dataframe and create a new column
df["status"] = df.apply(late_or_not, axis=1)

# Count the number of late and not late flights by origin and carrier
origin_count = df.groupby(["origin", "status"]).size().reset_index(name="count")
carrier_count = df.groupby(["carrier", "status"]).size().reset_index(name="count")

# Create a pivot table to show the number of late and not late flights by origin
origin_table = origin_count.pivot(index="origin", columns="status", values="count")
print(origin_table)

# Create a bar chart to show the number of late and not late flights by origin
origin_table.plot(kind="bar", stacked=True)
plt.title("Number of late and not late flights by origin")
plt.xlabel("Origin")
plt.ylabel("Count")
plt.legend(title="Status")
plt.show()

# Create a pivot table to show the number of late and not late flights by carrier
carrier_table = carrier_count.pivot(index="carrier", columns="status", values="count")
print(carrier_table)

# Create a bar chart to show the number of late and not late flights by carrier
carrier_table.plot(kind="bar", stacked=True)
plt.title("Number of late and not late flights by carrier")
plt.xlabel("Carrier")
plt.ylabel("Count")
plt.legend(title="Status")
plt.show()

# Calculate the average delay time by origin and carrier
origin_delay = df.groupby("origin")[["dep_delay", "arr_delay"]].mean().reset_index()
carrier_delay = df.groupby("carrier")[["dep_delay", "arr_delay"]].mean().reset_index()

# Calculate the total delay time by origin and carrier
origin_delay["total_delay"] = origin_delay["dep_delay"] + origin_delay["arr_delay"]
carrier_delay["total_delay"] = carrier_delay["dep_delay"] + carrier_delay["arr_delay"]

# Print the average and total delay time by origin and carrier
print(origin_delay)
print(carrier_delay)

# Create a scatter plot to show the total delay time by origin
plt.scatter(origin_delay["origin"], origin_delay["total_delay"])
plt.title("Total delay time by origin")
plt.xlabel("Origin")
plt.ylabel("Total delay time (minutes)")
plt.show()

# Create a scatter plot to show the total delay time by carrier
plt.scatter(carrier_delay["carrier"], carrier_delay["total_delay"])
plt.title("Total delay time by carrier")
plt.xlabel("Carrier")
plt.ylabel("Total delay time (minutes)")
plt.show()

# Calculate the total, average, mean, median of each carrier's flight distance
carrier_distance = df.groupby("carrier")["distance"].agg(["sum", "mean", "median"]).reset_index()
print(carrier_distance)
