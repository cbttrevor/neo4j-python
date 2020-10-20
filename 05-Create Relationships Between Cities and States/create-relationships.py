import neo4j
import json
import os

neo = neo4j.GraphDatabase.bolt_driver('localhost', auth=('neo4j', 'test'))
sess = neo.session()

script_dir = os.path.dirname(os.path.realpath(__file__))

with open('{0}/cities.json'.format(script_dir)) as cities:
    city_list = json.load(cities)

for city in city_list:
    query = 'MATCH (c:city {{ name: "{0}" }}), (s:state {{ abbreviation: "{1}" }}) MERGE (c)-[:EXISTS_IN]->(s)'.format(city['city'], city['state'])
    print(query)
    print(city)
    sess.run(query)