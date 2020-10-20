'''
This Python script demonstrates how to connect to Neo4j using the Bolt protocol.
'''

from neo4j import GraphDatabase

print('Connecting to Neo4j')
driver = GraphDatabase.bolt_driver('localhost', auth=('neo4j', 'test'))

print('Executing query against Neo4j')
session = driver.session()
result = session.run('MATCH (n) RETURN n;')
print(result.data())
print('Finished running query')

driver.close()
print('bolt driver has been closed')