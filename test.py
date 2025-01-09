import pandas as pd

file_path = 'Storm_Individual_Power_Outages.csv'
data = pd.read_csv(file_path)
print(data.shape)
data['start_time_local'] = pd.to_datetime(data['start_time_local'], format='mixed')

latest_records = data.loc[data.groupby('sensor_id')['start_time_local'].idxmax()]
print(latest_records.shape)
outage_time = "2025-12-31T23:59:59-06:00"
sensors_with_specific_outage = latest_records[latest_records['end_time_local'] == outage_time]

sensor_list = sensors_with_specific_outage['sensor_id'].unique().tolist()

print(len(sensor_list))

og_file = 'Sensor_Location.csv'

df = pd.read_csv(og_file)

df['outage'] = 'no'
df.loc[df['sensor_id'].isin(sensor_list), 'outage'] = 'yes'
df.to_csv('parsed.csv', index=False)