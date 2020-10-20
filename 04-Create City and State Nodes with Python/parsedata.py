'''
This Python script parses the list of US cities with a population exceeding 250,000 from geonames.org data.

You must place download the data separately and place us.txt in the same directory as this script.
'''

import os
import csv
import json

script_dir = os.path.dirname(os.path.realpath(__file__))

cities = []

with open('{0}\\us.txt'.format(script_dir), mode='r', encoding='utf-8', errors='ignore') as data:
    reader = csv.reader(data, delimiter='\t')
    for line in reader:
        try:
            if line[7].startswith('PPL') and int(line[14]) > 250000:
                result = {
                    'city': line[1],
                    'state': line[10],
                    'population': line[14]
                }
                print(result)
                cities.append(result)
                
        except Exception as ex:
            print(ex)
            #exit()
            #print('Failed to print line')

print(cities)
with open('{0}\\cities.json'.format(script_dir), mode='w') as cities_file:
    cities_file.write(json.dumps(cities))

print('Done')