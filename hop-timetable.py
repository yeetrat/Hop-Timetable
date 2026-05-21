import pandas as pd

# Load the wide format (original schedule)
df_wide = pd.read_csv('intermodal_schedule.csv')
print("Wide format:")
print(df_wide.head())

# Load the long format (best for analysis)
df_long = pd.read_csv('intermodal_schedule_long.csv')

# Convert departure_time back to datetime
df_long['departure_time'] = pd.to_datetime(df_long['departure_time'])

print("\nLong format:")
print(df_long.head())

