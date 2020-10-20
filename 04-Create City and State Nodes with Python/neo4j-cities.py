from neo4j import GraphDatabase
import json
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
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

# # Create all the nodes for each U.S. State
# for state in set(map(lambda city: city['state'], city_list)):
#     query = 'MERGE (n:state {{ name: "{0}" }})'.format(state)
#     session.run(query)   
#     print(state)