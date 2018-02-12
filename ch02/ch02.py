import json

filename = "usagov_bitly_data2013-05-17-1368832207.txt"

records = [json.loads(line) for line in open(filename, encoding='utf-8')]

time_zones = [rec['tz'] for rec in records if 'tz' in rec]

print(time_zones[:10])
