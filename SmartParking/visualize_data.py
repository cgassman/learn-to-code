import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt

# TODO reduce calculated values to two decimals
# TODO move 'startdate' to preparation of files

sns.set_theme(style="whitegrid")

# --- load data and add a column with date information only ---
parking_data_tramstr = pd.read_csv(r'data\df_parking_tramstr.csv')
parking_data_tramstr['startdate'] = pd.to_datetime(parking_data_tramstr['starttime']).dt.floor('D')

charging_data_tramstr = pd.read_csv(r'data\df_charging_tramstr.csv')
charging_data_tramstr['startdate'] = pd.to_datetime(charging_data_tramstr['Start time']).dt.floor('D')

# --- calculate figures per day in % ---
avg_parking_time_percent = parking_data_tramstr.groupby('weekday')['duration'].mean() * 100 / 1440
avg_charging_time_percent = charging_data_tramstr.groupby('Weekday')['Duration'].mean() * 100 / 1440

# --- calculate figures (min, avg, max) per day in absolute numbers ---
number_of_diff_dates_parking = parking_data_tramstr.groupby('weekday')['startdate'].value_counts()
number_of_diff_dates_parking_2 = number_of_diff_dates_parking.groupby('weekday').count()
avg_parking_events = parking_data_tramstr.groupby('weekday')['station'].count() / number_of_diff_dates_parking_2
print(avg_parking_events)

number_of_diff_dates_charging = charging_data_tramstr.groupby('Weekday')['startdate'].value_counts()
number_of_diff_dates_charging_2 = number_of_diff_dates_charging.groupby('Weekday').count()
avg_charging_events = charging_data_tramstr.groupby('Weekday')['Station'].count() / number_of_diff_dates_charging_2
print(avg_charging_events)

# to get the date from a datetime
# print(pd.to_datetime(parking_data_tramstr['starttime']).dt.floor('D'))

'''
min_parking_events = #TODO grouped by weekday: for each day calculate number of parking events and take min
max_parking_events = #TODO grouped by weekday: for each day calculate number of parking events and take max

min_charging_events = #TODO grouped by weekday: for each day calculate number of charging events and take min
max_charging_events = #TODO grouped by weekday: for each day calculate number of charging events and take max
'''


# rs = np.random.RandomState(365)
# values = rs.randn(365, 2).cumsum(axis=0)
# dates = pd.date_range("1 1 2016", periods=365, freq="D")
# data = pd.DataFrame(values, dates, columns=["Avg Parking in Percent", "Avg Charging in Percent"])
# data = data.rolling(7).mean()

# sns.lineplot(data=data, palette="tab10", linewidth=2.5)

# plt.show()