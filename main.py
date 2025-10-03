import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Read sheets from the excel file
task1=pd.read_excel("Data1.xlsx",sheet_name='Task 1')
task1.set_index("date",inplace=True)
task2=pd.read_excel("Data1.xlsx",sheet_name='Task 2')
task2.set_index("date",inplace=True)
task3=pd.read_excel("Data1.xlsx",sheet_name='Task 3')
task3.set_index("date",inplace=True)
# Task 1 Equity Analysis
# Task 1.1 Compute monthly returns from the price series for each index.
# Using pct_change function to calculate monthly returns and drop the NaN data (First 12 month with no rolling data)
task1_returns=task1.pct_change().dropna()
print(task1_returns)

task1_volatility=task1_returns.rolling(window=12).std()*np.sqrt(12)
# First calculate the standard deviation of the rolling 12 month data (.std()) then multiply by the square root of 12 (12 month period)
print(task1_volatility.dropna())

# plot rolling 12 month volatility
plt.figure(figsize=(12, 8))
# plot the graph for 6 different indices
for column in task1_volatility.columns:
    plt.plot(task1_volatility.index,task1_volatility[column],label=column)
# highlighting 2008, 2020 and 2022
highlight_years = [2008, 2020, 2022]
for year in highlight_years:
    plt.axvline(pd.Timestamp(f"{year}-01-01"), linestyle="--")
    plt.axvline(pd.Timestamp(f"{year}-12-31"), linestyle="--")
plt.xlabel("Date")
plt.ylabel("Volatility")
plt.legend()
plt.show()

# Find the returns of the indices in 3 years
year_return2008=task1_returns[task1_returns.index.year==2008]
year_return2020=task1_returns[task1_returns.index.year==2020]
year_return2022=task1_returns[task1_returns.index.year==2022]
# Calculate the volatility for each index in 3 years
index_volatility2008=year_return2008.std()*np.sqrt(12)
index_volatility2020=year_return2020.std()*np.sqrt(12)
index_volatility2022=year_return2022.std()*np.sqrt(12)
# Use idxmax() and max() function to identify the most volatile index and its volatility
print("The most volatile index in 2008 is",index_volatility2008.idxmax(), "with a volatility of" ,index_volatility2008.max(),
     ". The most volatile index in 2020 is", index_volatility2020.idxmax(), "with a volatility of" ,index_volatility2020.max(),
      ". The most volatile index in 2022 is", index_volatility2022.idxmax(), "with a volatility of" ,index_volatility2022.max())

# Creating a new column "Slope"
task2["Slope"]=task2["US10Y"]-task2["US2Y"]
plt.figure(figsize=(12, 8))
plt.plot(task2.index,task2["Slope"],color="red")

plt.figure(figsize=(12, 8))
plt.plot(task2.index,task2["Slope"],color="red")
# Using fill_between function to identify and shade periods with negative slope
plt.fill_between(task2.index, task2['Slope'], 1, where=task2['Slope'] < 0, color='grey')

# Task 3 Crypto Correlation
task3_returns=task3.pct_change().dropna()
print(task3_returns)

rolling_corr=task3_returns["BTC_Price"].rolling(window=12).corr(task3_returns["ETH_Price"]).dropna()
print(rolling_corr)
plt.figure(figsize=(12,6))
plt.plot(rolling_corr.index,rolling_corr)
plt.title('Rolling 12-Week Correlation')
plt.xlabel('Date')
plt.ylabel('Correlation Coefficient')
plt.show()

# Using idxmax/min function to identify the date of the largest/lowest correlation
max_corr_period=rolling_corr.idxmax()
min_corr_period=rolling_corr.idxmin()
print("A period of high correlation is around",max_corr_period)
print("A period of high correlation is around",min_corr_period)
