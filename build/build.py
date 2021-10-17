import json
import os

m = '{ "motorcycles": [] }'
y = json.loads(m)

entries = os.listdir('../vehicle/source/')
for entry in entries:
    print('adding vehicle ' + entry)
    with open('../vehicle/source/'+entry) as vehicle:
        vehicle_json = json.load(vehicle)
        y['motorcycles'].append(vehicle_json['motorcycle'])

with open('../vehicle/motorcycles.json', 'w') as outfile:
    json.dump(y, outfile, indent=2, ensure_ascii=False)
