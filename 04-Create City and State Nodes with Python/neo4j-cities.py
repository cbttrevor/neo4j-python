'''
This Python script will create nodes in Neo4j that represent cities with more than 100,000 population, from cities.json.

The cities.json file must exist in the same directory as this Python script.
'''

from neo4j import GraphDatabase
import json
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
print(script_dir)
n4j = GraphDatabase.bolt_driver('localhost', auth=('neo4j', 'test'))
session = n4j.session()

city_list = ''

with open('{0}\\cities.json'.format(script_dir)) as cities:
    city_list = json.loads(cities.read())

# Create nodes for each city in the United States
for city in city_list:
    print(city)
    query = 'MERGE (n:city {{ name: "{0}" }})'.format(city['city'])
    session.run(query)
