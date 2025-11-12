import pandas as pd

pd.set_option
df = pd.read_csv("Building_Permits.csv", low_memory=False)

print(df.info())

print(df.describe(include="object"))
Q1 = df.quantile(0.25, numeric_only=True)
Q3 = df.quantile(0.75, numeric_only=True)

# Calculate the Interquartile Range (IQR)
# IQR = Q3 - Q1
# print(IQR)
# Exploratory Data Analysis

# 1. Descriptive Statistics
#   a. Central tendency
#   b. data spread
# 2. Visualization


# Central Tendency

corr = df.corr(numeric_only=True)

print(corr)
