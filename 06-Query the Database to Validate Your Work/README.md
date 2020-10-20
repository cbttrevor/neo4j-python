## Learning Objective

Now that you've successfully imported cities and states into Neo4j, let's validate your work.
The query below will return all cities and states with relationships connecting them.

```
MATCH (c:city)-[r:EXISTS_IN]->(s:state),(s:state) RETURN c,r,s;
```