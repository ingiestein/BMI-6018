import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pd.set_option('display.max_columns',None)


flights_data = pd.read_csv("data/flights.csv", index_col=0)
weather_data_pd = pd.read_csv("data/weather.csv", index_col=0)
weather_data_np = weather_data_pd.to_numpy()

# print(flights_data.head(5))
# q_1
jfk_to_slc_mask = (flights_data["origin"] == "JFK") & (flights_data["dest"] == "SLC")
q_1 = jfk_to_slc_mask.sum()
print("q_1: ", q_1)

#q_2
to_slc_mask = flights_data["dest"] == "SLC"
unique_airlines_to_slc = flights_data[to_slc_mask]["carrier"].unique()
q_2 = len(unique_airlines_to_slc)
print("q_2: ", q_2)

#q_3
delay_RDU_mask = flights_data["dest"] == "RDU"
#.mean() autoskips NA fields
q_3 = delay = flights_data[delay_RDU_mask]["arr_delay"].mean()
print("q_3: ", q_3)

#q_4
total_to_SEA_mask = flights_data["dest"] == "SEA"
LGA_to_SEA_mask = (flights_data["origin"] == "LGA") & (flights_data["dest"] == "SEA")
JFK_to_SEA_mask = (flights_data["origin"] == "JFK") & (flights_data["dest"] == "SEA")

total_to_SEA = total_to_SEA_mask.sum()
q_4 = (LGA_to_SEA_mask.sum() + JFK_to_SEA_mask.sum())/total_to_SEA_mask.sum()
print("q_4: ", q_4)


#q_5
#convers the year month day columns to a single date colum (following formatting requested)
flights_data["date"] = pd.to_datetime(flights_data[['year', 'month', 'day']]).dt.strftime('%Y/%m/%d')
#then you group all the columns by date, average for each date, then sort so the largest is at top, then take the first value
# the .mean() method by default drops NA values
q_5 = flights_data.groupby("date")["dep_delay"].mean().sort_values(ascending=False).iloc[0]
print("q_5: ", q_5)

#q_6
q_6 = flights_data.groupby("date")["arr_delay"].mean().sort_values(ascending=False).iloc[0]
print("q_6: ", q_6)

#q_7
#create colum of speed = distance/air_time
flights_data["speed"] = flights_data["distance"] / flights_data["air_time"]
#filter for year 2013, select LGA or JFK as origin, find tail number and speed columns, sort by largest speed at top, select first entry
q_7 = flights_data[(flights_data["year"] == 2013) & ((flights_data["origin"] == "LGA") | (flights_data["origin"] == "JFK"))][["tailnum", "speed"]].sort_values(ascending=False, by="speed").iloc[0]
print("q_7: ", q_7)


#q_8
#use the fillna method to replace all na with 0 in the dataframe
q_8 = weather_data_pd.fillna(0)
print("q_8: ", q_8.head(5))


#q9
#converstion to np removes column names, so have to choose the correct column numerically.
mask = weather_data_np[:, 2]==2
q_9 = len(weather_data_np[mask])
print("q_9: ", q_9)

#q_10
q_10 = weather_data_np[mask][:,7].mean() #taking the mean of the index 7 column (humidity) and getting the mean.
print("q_10: ", q_10)

#q11
q_11 = weather_data_np[mask][:,7].std()
print("q_11: ", q_11)