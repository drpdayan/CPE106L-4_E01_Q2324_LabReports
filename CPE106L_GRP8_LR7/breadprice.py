import pandas as pd

from matplotlib import pyplot as plt


frame = pd.read_csv("breadprice.csv")
# print(frame)

#Cleaning the data
frame.dropna(inplace = True)
theCopy = frame.dropna() 
print(frame)

# Calculate the average price per year
yearly_avg_price = frame.groupby('Year').mean()

# Extract year and average price for plotting
years = yearly_avg_price.index
avg_prices = yearly_avg_price['Jan'] 

# Plot the average price per year
plt.plot(years, avg_prices, marker='*', color = 'red')
plt.xlabel('Year')
plt.ylabel('Average Bread Price')
plt.title('Average Bread Price per Year')
plt.grid(True)
plt.show()

