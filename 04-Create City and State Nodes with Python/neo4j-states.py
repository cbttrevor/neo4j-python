import json
import os
import neo4j

script_dir = os.path.dirname(os.path.realpath(__file__))

try:
    n4j = neo4j.GraphDatabase.bolt_driver('localhost', auth=('neo4j', 'test'))
    sess = n4j.session()
except neo4j.exceptions.ServiceUnavailable as ex:
    print('Could not connect to Neo4j instance. Is your development container running?')
    exit()

with open('{0}\\states.json'.format(script_dir), mode='r') as states:
    state_list = json.load(states)

for state in state_list:
    print(state['name'])
    print(state['abbreviation'])
    query = 'MERGE (s:state {{ name: "{0}", abbreviation: "{1}" }})'.format(state['name'], state['abbreviation'])
    print(query)
    sess.run(query)