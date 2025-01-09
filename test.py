import pandas as pd

file_path = 'Storm_Individual_Power_Outages.csv'
data = pd.read_csv(file_path)

outage_time = "2025-12-31T19:59:59-08:00"
sensors_with_specific_outage = data[data['end_time_local'] == outage_time]

sensor_list = sensors_with_specific_outage['sensor_id'].unique().tolist()

print(len(sensor_list))

og_file = 'Sensor_Location.csv'

df = pd.read_csv(og_file)

df['outage'] = 'no'
df.loc[df['sensor_id'].isin(sensor_list), 'outage'] = 'yes'
df.to_csv('parsed.csv', index=False)