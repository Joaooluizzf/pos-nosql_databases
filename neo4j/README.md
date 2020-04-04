# pos-nosql_databases

## Exercício 1

Exercise 1.1: Retrieve all nodes from the database 

```
match (n) return n
```

Exercise 1.2: Examine the schema of your database

```
CALL db.schema()
```

Exercise 1.3: Retrieve all Person nodes 

```
match (p:Person) return p
```

Exercise 1.4: Retrieve all Movie nodes

```
match (m:Movie) return m
```

## Exercício 2

Exercise 2.1: Retrieve all movies that were released in a specific year

```
match (m:Movie {released:2003}) return m
```

Exercise 2.2: View the retrieved results as a table

```
clicar no ícone de tabela
```

Exercise 2.3: Query the database for all property keys

```
CALL db.propertyKeys
```

Exercise 2.4: Retrieve all Movies released in a specific year, returning their titles

```
match (m:Movie {released: 2006}) return m.title
```

Exercise 2.5: Display title, released, and tagline values for every Movie node in the graph

```
match (m:Movie) return m.title, m.released, m.tagline
```

Exercise 2.6: Display more user-friendly headers in the table

```
match (m:Movie) return m.title as `movie title`, m.released as released, m.tagline as tagLine
```

## Exercício 3

Exercise 3.1: Display the schema of the database

```
CALL db.schema
```

Exercise 3.2: Retrieve all people who wrote the movie Speed Racer

```
match (p:Person)-[:WROTE]->(:Movie {title: 'Speed Racer'}) return p.name
```

Exercise 3.3: Retrieve all movies that are connected to the person, Tom Hanks

```
match (m:Movie)<--(:Person {name: 'Tom Hanks'}) return m.title
```

Exercise 3.4: Retrieve information about the relationships Tom Hanks has with the set of movies retrieved earlier

```
match (m:Movie)-[rel]-(:Person {name: 'Tom Hanks'}) return m.title, type(rel)
```

Exercise 3.5: Retrieve information about the roles that Tom Hanks acted in

```
match (m:Movie)-[rel:ACTED_IN]-(:Person {name: 'Tom Hanks'}) return m.title, rel.roles
```

## Exercício 4

Exercise 4.1: Retrieve all movies that Tom Cruise acted in

```
match (a:Person)-[:ACTED_IN]->(m:Movie)
where a.name = 'Tom Cruise'
return m.title as Movie
```

Exercise 4.2: Retrieve all people that were born in the 70’s

```
match (a:Person)
where a.born >= 1970 AND a.born < 1980
return a.name as Name, a.born as `Year Born`
```

Exercise 4.3: Retrieve the actors who acted in the movie The Matrix who were born after 1960

```
match (a:Person)-[:ACTED_IN]->(m:Movie)
where a.born > 1960 AND m.title = 'The Matrix'
return a.name as Name, a.born as `Year Born`
```

Exercise 4.4: Retrieve all movies by testing the node label and a property

```
match (m)
where m:Movie AND m.released = 2000
return m.title
```

Exercise 4.5: Retrieve all people that wrote movies by testing the relationship between two nodes

```
match (a)-[rel]->(m)
where a:Person AND type(rel) = 'WROTE' AND m:Movie
return a.name as Name, m.title as Movie
```

Exercise 4.6: Retrieve all people in the graph that do not have a property 

```
match (a:Person)
where not exists(a.born)
return a.name as Name
```

Exercise 4.7: Retrieve all people related to movies where the relationship has a property

```
match (a:Person)-[rel]->(m:Movie)
where exists(rel.rating)
return a.name as Name, m.title as Movie, rel.rating as Rating
```

Exercise 4.8: Retrieve all actors whose name begins with James

```
match (a:Person)-[:ACTED_IN]->(:Movie)
where a.name STARTS with 'James'
return a.name
```

Exercise 4.9: Retrieve all REVIEWED relationships from the graph with filtered results

```
match (:Person)-[r:REVIEWED]->(m:Movie)
where toLower(r.summary) CONTAINS 'fun'
return  m.title as Movie, r.summary as Review, r.rating as Rating
```

Exercise 4.10: Retrieve all people who have produced a movie, but have not directed a movie

```
match (a:Person)-[:PRODUCED]->(m:Movie)
where not ((a)-[:DIRECTED]->(:Movie))
return a.name, m.title
```

Exercise 4.11: Retrieve the movies and their actors where one of the actors also directed the movie

```
match (a1:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(a2:Person)
where exists( (a2)-[:DIRECTED]->(m) )
return  a1.name as Actor, a2.name as `Actor/Director`, m.title as Movie
```

Exercise 4.12: Retrieve all movies that were released in a set of years

```
match (m:Movie)
where m.released in [2000, 2004, 2008]
return m.title, m.released
```

Exercise 4.13: Retrieve the movies that have an actor’s role that is the name of the movie

```
match (a:Person)-[r:ACTED_IN]->(m:Movie)
where m.title in r.roles
return  m.title as Movie, a.name as Actor
```

## Exercício 5

Exercise 5.1: Retrieve data using multiple match patterns

```
match (a:Person)-[:ACTED_IN]->(m:Movie)<-[:DIRECTED]-(d:Person),(a2:Person)-[:ACTED_IN]->(m)
where a.name = 'Gene Hackman'
return m.title as movie, d.name as director , a2.name as `co-actors`
```

Exercise 5.2: Retrieve particular nodes that have a relationship

```
match (p1:Person)-[:FOLLOWS]-(p2:Person)
where p1.name = 'James Thompson'
return p1, p2
```

Exercise 5.3: Modify the query to retrieve nodes that are exactly three hops away 

```
match (p1:Person)-[:FOLLOWS*3]-(p2:Person)
where p1.name = 'James Thompson'
return p1, p2
```

Exercise 5.4: Modify the query to retrieve nodes that are one and two hops away

```
match (p1:Person)-[:FOLLOWS*1..2]-(p2:Person)
where p1.name = 'James Thompson'
return p1, p2
```

Exercise 5.5: Modify the query to retrieve particular nodes that are connected no matter how many hops are required 

```
match (p1:Person)-[:FOLLOWS*]-(p2:Person)
where p1.name = 'James Thompson'
return p1, p2
```

Exercise 5.6: Specify optional data to be retrieved during the query

```
match (p:Person)
where p.name STARTS with 'Tom'
optional match (p)-[:DIRECTED]->(m:Movie)
return p.name, m.title
```

Exercise 5.7: Retrieve nodes by collecting a list

```
match (p:Person)-[:ACTED_IN]->(m:Movie)
return p.name as actor, collect(m.title) as `movie list`
```

Exercise 5.8: Retrieve all movies that Tom Cruise has acted in and the co-actors that acted in the same movie by collecting a list

```
match (p:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(p2:Person)
where p.name ='Tom Cruise'
return m.title as movie, collect(p2.name) as `co-actors`
```

Exercise 5.9: Retrieve nodes as lists and return data associated with the corresponding lists

```
match (p:Person)-[:REVIEWED]->(m:Movie)
return m.title as movie, count(p) as numReviews, collect(p.name) as reviewers
```

Exercise 5.10: Retrieve nodes and their relationships as list 

```
match (d:Person)-[:DIRECTED]->(m:Movie)<-[:ACTED_IN]-(a:Person)
return d.name as director, count(a) as `number actors` , collect(a.name) as `actors worked with`
```

Exercise 5.11: Retrieve the actors who have acted in exactly five movies

```
match (a:Person)-[:ACTED_IN]->(m:Movie)
with  a, count(a) as numMovies, collect(m.title) as movies
where numMovies = 5
return a.name, movies
```

Exercise 5.12: Retrieve the movies that have at least 2 directors with other optional data

```
match (m:Movie)
with m, size((:Person)-[:DIRECTED]->(m)) as directors
where directors >= 2
optional match (p:Person)-[:REVIEWED]->(m)
return  m.title, p.name
```

## Exercício 6

Exercise 6.1: Execute a query that returns duplicate records.

```
match (a:Person)-[:ACTED_IN]->(m:Movie)
where m.released >= 1990 AND m.released < 2000
return DISTINCT m.released, m.title, collect(a.name)
```

Exercise 6.2: Modify the query to eliminate duplication

```
match (a:Person)-[:ACTED_IN]->(m:Movie)
where m.released >= 1990 AND m.released < 2000
return  m.released, collect(m.title), collect(a.name)
```

Exercise 6.3: Modify the query to eliminate more duplication.

```
match (a:Person)-[:ACTED_IN]->(m:Movie)
where m.released >= 1990 AND m.released < 2000
return  m.released, collect(DISTINCT m.title), collect(a.name)
```

Exercise 6.4: Sort results returned 

```
match (a:Person)-[:ACTED_IN]->(m:Movie)
where m.released >= 1990 AND m.released < 2000
return  m.released, collect(DISTINCT m.title), collect(a.name)
order by m.released DESC
```

Exercise 6.5: Retrieve the top 5 ratings and their associated movies

```
match (:Person)-[r:REVIEWED]->(m:Movie)
return  m.title as movie, r.rating as rating
order by r.rating DESC LIMIT 5
```

Exercise 6.6: Retrieve all actors that have not appeared in more than 3 movies

```
match (a:Person)-[:ACTED_IN]->(m:Movie)
with  a,  count(a) as numMovies, collect(m.title) as movies
where numMovies <= 3
return a.name, movies
```

## Exercício 7


Exercise 7.1: Collect and use lists

```
match (a:Person)-[:ACTED_IN]->(m:Movie), (m)<-[:PRODUCED]-(p:Person)
with  m, collect(DISTINCT a.name) as cast, collect(DISTINCT p.name) as producers
return DISTINCT m.title, cast, producers
order by size(cast)
```

Exercise 7.2: Collect a list 

```
match (p:Person)-[:ACTED_IN]->(m:Movie)
with p, collect(m) as movies
where size(movies)  > 5
return p.name, movies
```

Exercise 7.3: Unwind a list

```
match (p:Person)-[:ACTED_IN]->(m:Movie)
with p, collect(m) as movies
where size(movies)  > 5
with p, movies UNWIND movies as movie
return p.name, movie.title
```

Exercise 7.4: Perform a calculation with the date type

```
match (a:Person)-[:ACTED_IN]->(m:Movie)
where a.name = 'Tom Hanks'
return  m.title, m.released, date().year  - m.released as yearsAgoReleased, m.released  - a.born as `age of Tom`
order by yearsAgoReleased
```

## Exercício 8

Exercise 8.1: Create a Movie node

```
create (:Movie {title: 'Forrest Gump'})
```

Exercise 8.2: Retrieve the newly-created node

```
match (m:Movie)
where m.title = 'Forrest Gump'
return m
```

Exercise 8.3: Create a Person node

```
create (:Person {name: 'Robin Wright'})
```

Exercise 8.4: Retrieve the Person node you just created by its name

```
match (p:Person)
where p.name = 'Robin Wright'
return p
```

Exercise 8.5: Add a label to a node

```
match (m:Movie)
where m.released < 2010
set m:OlderMovie
return DISTINCT labels(m)
```

Exercise 8.6: Retrieve the node using the new label 

```
match (m:OlderMovie)
return m.title, m.released
```

Exercise 8.7: Add the Female label to selected nodes

```
match (p:Person)
where p.name STARTS with 'Robin'
set p:Female
```

Exercise 8.8: Retrieve all Female nodes

```
match (p:Female)
return p.name
```

Exercise 8.9: Remove the Female label from the nodes that have this label

```
match (p:Female)
remove p:Female
```

Exercise 8.10: View the current schema of the graph

```
CALL db.schema
```

Exercise 8.11: Add properties to a movie

```
match (m:Movie)
where m.title = 'Forrest Gump'
set m:OlderMovie, m.released = 1994, m.tagline = "Life is like a box of chocolates...you never know what you're gonna get.", m.lengthInMinutes = 142
```

Exercise 8.12: Retrieve an OlderMovie node to confirm the label and properties

```
match (m:OlderMovie)
where m.title = 'Forrest Gump'
return m
```

Exercise 8.13: Add properties to the person, Robin Wright

```
match (p:Person)
where p.name = 'Robin Wright'
set p.born = 1966, p.birthPlace = 'Dallas'
```

Exercise 8.15: Remove a property from a Movie node

```
match (m:Movie)
where m.title = 'Forrest Gump'
set m.lengthInMinutes = null
```

Exercise 8.16: Retrieve the node to confirm that the property has been removed 

```
match (m:Movie)
where m.title = 'Forrest Gump'
return m
```

Exercise 8.17: Remove a property from a Person node_

```
match (p:Person)
where p.name = 'Robin Wright'
remove p.birthPlace
```

Exercise 8.18: Retrieve the node to confirm that the property has been removed

```
match (p:Person)
where p.name = 'Robin Wright'
return p
```

## Exercício 9

Exercise 9.1: Create ACTED_IN relationships

```
match (m:Movie)
where m.title = 'Forrest Gump'
match (p:Person)
where p.name = 'Tom Hanks' OR p.name = 'Robin Wright' OR p.name = 'Gary Sinise'
create (p)-[:ACTED_IN]->(m)
```

Exercise 9.2: Create DIRECTED relationships

```
match (m:Movie)
where m.title = 'Forrest Gump'
match (p:Person)
where p.name = 'Robert Zemeckis'
create (p)-[:DIRECTED]->(m)
```

Exercise 9.3: Create a HELPED relationship

```
match (p1:Person)
where p1.name = 'Tom Hanks'
match (p2:Person)
where p2.name = 'Gary Sinise'
create (p1)-[:HELPED]->(p2)
```

Exercise 9.4: Query nodes and new relationships

```
match (p:Person)-[rel]-(m:Movie)
where m.title = 'Forrest Gump'
return p, rel, m
```

Exercise 9.5: Add properties to relationships

```
match (p:Person)-[rel:ACTED_IN]->(m:Movie)
where m.title = 'Forrest Gump'
set rel.roles =
case p.name
when 'Tom Hanks' THEN ['Forrest Gump']
when 'Robin Wright' THEN ['Jenny Curran']
when 'Gary Sinise' THEN ['Lieutenant Dan Taylor']
end
```

Exercise 9.6: Add a property to the HELPED relationship

```
match (p1:Person)-[rel:HELPED]->(p2:Person)
where p1.name = 'Tom Hanks' AND p2.name = 'Gary Sinise'
set rel.research = 'war history'
```

Exercise 9.7: View the current list of property keys in the graph

```
call db.propertyKeys
```

Exercise 9.8: View the current schema of the graph

```
call db.schema
```

Exercise 9.9: Retrieve the names and roles for actors

```
match (p:Person)-[rel:ACTED_IN]->(m:Movie)
where m.title = 'Forrest Gump'
return p.name, rel.roles
```

Exercise 9.10: Retrieve information about any specific relationships

```
match (p1:Person)-[rel:HELPED]-(p2:Person)
return p1.name, rel, p2.name
```

Exercise 9.11: Modify a property of a relationship

```
match (p:Person)-[rel:ACTED_IN]->(m:Movie)
where m.title = 'Forrest Gump' AND p.name = 'Gary Sinise'
set rel.roles =['Lt. Dan Taylor']
```

Exercise 9.12: Remove a property from a relationship

```
match (p1:Person)-[rel:HELPED]->(p2:Person)
where p1.name = 'Tom Hanks' AND p2.name = 'Gary Sinise'
REMOVE rel.research
```

Exercise 9.13: Confirm that your modifications were made to the graph 

```
match (p:Person)-[rel:ACTED_IN]->(m:Movie)
where m.title = 'Forrest Gump'
return p, rel, m
```

## Exercício 10

Exercise 10.1: Delete a relationship

```
match (:Person)-[rel:HELPED]-(:Person)
delete rel
```

Exercise 10.2: Confirm that the relationship has been deleted 

```
match (:Person)-[rel:HELPED]-(:Person)
return rel
```

Exercise 10.3: Retrieve a movie and all of its relationships

```
match (p:Person)-[rel]-(m:Movie)
where m.title = 'Forrest Gump'
return p, rel, m
```

Exercise 10.4: Try deleting a node without detaching its relationships

```
match (m:Movie)
where m.title = 'Forrest Gump'
delete m
```

Exercise 10.5: Delete a Movie node, along with its relationships 

```
match (m:Movie)
where m.title = 'Forrest Gump'
detach delete m
```

Exercise 10.6: Confirm that the Movie node has been deleted

```
match (p:Person)-[rel]-(m:Movie)
where m.title = 'Forrest Gump'
return p, rel, m
```
