'''
This Python script demonstrates how to retrieve results from Neo4j database queries.
'''

from neo4j import GraphDatabase as n4j

bolt = n4j.bolt_driver('localhost', auth=('neo4j', 'test'))
sess = bolt.session()

result = sess.run('MATCH (c:city)-[r:EXISTS_IN]->(s:state) RETURN c,r,s;')

[print(city) for city in result.values()]