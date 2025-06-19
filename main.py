""""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.options.display.width=0
df =pd.read_csv("C:/Users/Amit/Downloads/apple_products (1).csv")
print(df)
print(df.isnull().sum()) #.isnull use for checking that is there any null value is available
print(df.describe()) # .describe is use for checking all numeric data , "count , min value ,max value ,mean etc"
Highest_rated=df.sort_values(by=["Star Rating"],ascending=False)
Highest_rated= Highest_rated.head(10)
print(Highest_rated["Product Name"])
iphone=Highest_rated["Product Name"].value_counts()
labels= Highest_rated["Product Name"]
counts= Highest_rated["Number Of Ratings"]
figure=plt.bar(Highest_rated, x=labels, y=counts, title="Nubmer of rating of highest rated iphone")
figure.show()"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.display.width = 0
df = pd.read_csv("C:/Users/Amit/Downloads/apple_products (1).csv")

print(df)
print(df.isnull().sum())  # Checking for null values
print(df.describe())  # Summary statistics for numeric data

Highest_rated = df.sort_values(by=["Star Rating"], ascending=False)
Highest_rated = Highest_rated.head(10)
print(Highest_rated["Product Name"])

iphone = Highest_rated["Product Name"].value_counts()
labels = Highest_rated["Product Name"]  # Using the product names directly
counts = Highest_rated["Number Of Ratings"]
counting = Highest_rated["Number Of Reviews"]

plt.figure(figsize=(10, 6))
plt.bar(labels, counting)
plt.title("Number of ratings of highest rated iPhones")
plt.xlabel("Product Name")
plt.ylabel("Number of Ratings")
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent label cutoff
plt.show()
plt.figure(figsize=(10, 6))
plt.bar(labels, counts)
plt.title("Number of reviews of highest rated iPhones")
plt.xlabel("Product Name")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent label cutoff
plt.show()
sales= Highest_rated["Sale Price"]
plt.figure(figsize=(10, 6))
plt.scatter(df["Number Of Ratings"],df["Sale Price"] )

# Calculate and plot trendline (linear regression)
z = np.polyfit( df["Number Of Ratings"],df["Sale Price"], 1)  # 1 = linear trend
p = np.poly1d(z)  # Create a polynomial function
plt.plot(df["Sale Price"], p(df["Sale Price"]), 'r--', label='Trendline')
plt.title("Realation between sales and number of rating")
plt.tight_layout()  # Adjust layout to prevent label cutoff
plt.show()
"""Scatter Plot (plt.scatter)

x = df["Sale Price"] → X-axis (Sale Price)

y = df["Number Of Ratings"] → Y-axis (Number of Ratings)

alpha=0.6 → Makes points slightly transparent to avoid overplotting.

color='blue' → Sets the color of the points.

Trendline Calculation (np.polyfit)

np.polyfit(x, y, 1) → Fits a linear regression (degree=1) to the data.

np.poly1d(z) → Creates a function for the trendline equation (y = mx + c).

Plotting the Trendline (plt.plot)

Uses the predicted values from p(df["Sale Price"]).

'r--' → Red dashed line for the trendline."""

plt.figure(figsize=(10, 6))
plt.scatter(df["Number Of Ratings"],df["Discount Percentage"] )
z = np.polyfit( df["Number Of Ratings"],df["Discount Percentage"], 1)  # 1 = linear trend
p = np.poly1d(z)  # Create a polynomial function
plt.plot(df["Sale Price"], p(df["Sale Price"]), 'r--', label='Trendline')
plt.title("Realation between Discount Percentage and number of rating")
plt.tight_layout()  # Adjust layout to prevent label cutoff
plt.show()