## Learning Objective

Now that your development environment is set up, let's explore how to connect to Neo4j from Python.
You can always refer back to the [Neo4j developer documentation](https://neo4j.com/developer/python/) as we move forward.

First, import the `GraphDatabase` class.

```
from neo4j import GraphDatabase
```

Next, use the `bolt_driver()` method to connect to the database engine.
The username and password are passed as a tuple.

```
driver = GraphDatabase.bolt_driver('localhost', auth=('user', 'pass'))
```

Finally, create a session from the driver.

```
sess = driver.session()
```

You can use the session object to run a query against Neo4j.

```
sess.run('MATCH (n) RETURN n;')
```