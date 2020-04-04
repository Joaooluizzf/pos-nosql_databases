# pos-nosql_databases

## Exercício 1 - Aquecendo com os pets

### 1. Adicione outro Peixe e um Hamster com nome Frodo

```javascript
db.pets.insert({name: "Frodo", species: "Peixe"})
db.pets.insert({name: "Frodo", species: "Hamster"})
```

### 2. Faça uma contagem dos pets na coleção

```javascript
db.pets.find().count()
```

### 3. Retorne apenas um elemento o método prático possível

```javascript
db.findOne()
```

### 4. Identifique o ID para o Gato Kilha.

```javascript
db.pets.findOne({name: 'Kilha', {_id: 1}})
```

### 5. Faça uma busca pelo ID e traga o Hamster Mike

```javascript
db.pets.find({_id: ObjectId("5e61b49fc42d8266db1e17b0")})
```

### 6. Use o find para trazer todos os Hamsters

```javascript
db.pets.find({species: "Hamster"})
```


### 7. Use o find para listar todos os pets com nome Mike

```javascript
db.pets.find({name: "Mike"})
```

### 8. Liste apenas o documento que é um Cachorro chamado Mike

```javascript
db.pets.find({name: "Mike", species: "Cachorro"})
```

## Exercício 2 - Mama mia!

### 1.Liste/Conte todas as pessoas que tem exatamente 99 anos. Você pode usar um count para indicar a quantidade.

```javascript
db.italians.find({age: 99}).count()
```

### 2. Identifique quantas pessoas são elegíveis atendimento prioritário (pessoas com mais de 65 anos)

```javascript
db.italians.find({age: {$gt: 65}}).count()
``` 

### 3. Identifique todos os jovens (pessoas entre 12 a 18 anos).

```javascript
db.italians.find({age: {$gte: 12, $lte: 18}})
```

### 4. Identifique quantas pessoas tem gatos, quantas tem cachorro e quantas não tem nenhum dos dois

```javascript
db.italians.find({cat: {$exists: 1}}).count()
db.italians.find({dog: {$exists: true}}).count()
db.italians.find({$and: [{dog: null}, {cat: null}]}).count()
```

### 5. Liste/Conte todas as pessoas acima de 60 anos que tenham gato

```javascript
db.italians.find({$and: [{age: {$gt: 60}}, {cat: {$exists: true}}]}).count()
```

### 6. Liste/Conte todos os jovens com cachorro

```javascript
db.italians.find({dog: {$exists: 1}, age: {$lte: 18}}).count()
```

### 7. Utilizando o $where, liste todas as pessoas que tem gato e cachorro

```javascript
db.italians.find({$where: function() { return this.cat && this.dog}},{"firstname":1,"cat":1,"dog":1,"_id":0})
```

### 8. Liste todas as pessoas mais novas que seus respectivos gatos.

```javascript
db.italians.find({$and: [{$where: "this.cat != null"}, {$where: "this.age < this.cat.age"}]})
```

### 9. Liste as pessoas que tem o mesmo nome que seu bichano (gatou ou cachorro)

```javascript
db.italians.find({$and: [{$where: "this.cat != null"}, {$where: "this.firstname == this.cat.name"}]}, {$and: [{$where: "this.dog != null"}, {$where: "this.firstname == this.dog.name"}]})
```

### 10. Projete apenas o nome e sobrenome das pessoas com tipo de sangue de fator RH negativo

```javascript
db.italians.find({bloodType : {$exists:  "-"}}, {firstname : true, surname: true})
```

### 11. Projete apenas os animais dos italianos. Devem ser listados os animais com nome e idade. Não mostre o identificado do mongo (ObjectId)

```javascript
db.italians.find({$where: "this.cat || this.dog"}, {"cat.name":1,"cat.age": 1, "dog.name":1, "dog.age":1,_id:0})
```

### 12. Quais são as 5 pessoas mais velhas com sobrenome Rossi?

```javascript
db.italians.find({surname:"Rossi"}).limit(5).sort({"age":-1})
```

### 13. Crie um italiano que tenha um leão como animal de estimação. Associe um nome e idade ao bichano

```javascript
db.italians.insert({name: "Aurélio", lion: {name: "Jasinski", age: 11}})
```

### 14. Infelizmente o Leão comeu o italiano. Remova essa pessoa usando o Id.

```javascript
db.italians.remove({_id: ObjectId("5e5a5322b7ae8d807156442a")})
```

### 15. Passou um ano. Atualize a idade de todos os italianos e dos bichanos em 1.

```javascript
db.italians.update({}, {"$inc": {"age": 1}}, {multi: true})
db.italians.update({cat: {$exists: true}}, {"$inc": {"cat.age": 1}}, {multi: true})
db.italians.update({dog: {$exists: true}}, {"$inc": {"dog.age": 1}}, {multi: true})
```


### 16. O Corona Vírus chegou na Itália e misteriosamente atingiu pessoas somente com gatos e de 66 anos. Remova esses italianos.


```javascript
db.italians.remove({age: {$eq: 66}, cat: {$exists: 1}})
```

### 17. Utilizando o framework agregate, liste apenas as pessoas com nomes iguais a sua respectiva mãe e que tenha gato ou cachorro.

```javascript
db.italians.aggregate([ {"$match": { mother: {$exists: true}, $or: [{cat: {$exists: true}}, {dog: {$exists: true}}] }}, {"$project": { "firstname": 1, "mother": 1, "cat":1, "dog":1, "isEqual": {"$cmp": ["$firstname", "$mother.firstname"]} }}, {"$match": {"isEqual": 0}}])
```

### 18. Utilizando aggregate framework, faça uma lista de nomes única de nomes. Faça isso usando apenas o primeiro nome

```javascript
db.italians.aggregate([{$group: { _id: "$firstname"}}])
```


### 19. Agora faça a mesma lista do item acima, considerando nome completo.

```javascript
db.italians.aggregate({$group: {_id: {name:"$firstname", surname: "$surname"}}})
```

### 20. Procure pessoas que gosta de Banana ou Maçã, tenham cachorro ou gato, mais de 20 e menos de 60 anos.

```javascript
db.italians.find({age: {$gt: 20, $lt: 60}, favFruits: {$all: ["Banana", "Maçã"]}, $where: "this.cat" || "this.dog"})
```

## Exercício 3 - Stockbrokers


### 1. Liste as ações com profit acima de 0.5 (limite a 10 o resultado)

```javascript
db.stocks.find({"Profit Margin": {$gt: 0.5}}).limit(10)
```

### 2. Liste as ações com perdas (limite a 10 novamente)
```javascript
db.stocks.find({"Profit Margin": {"$lt": 0}},{"Profit Margin":1,_id:0}).sort({"Profit Margin": 1}).limit(10)
```

### 3. Liste as 10 ações mais rentáveis

```javascript
db.stocks.find({}).sort({"Profit Margin":-1}).limit(10)
```

### 4. Qual foi o setor mais rentável?
```javascript
db.stocks.aggregate([{ $group: { _id: "$Sector", Profits: {$sum: "$Profit Margin"} }}, { $sort: { "Profits": -1 }} ])
```

### 5. Ordene as ações pelo profit e usando um cursor, liste as ações.
```javascript
var cursor = db.stocks.find({"Profit Margin": {$exists: true}}, {"Company": 1, "Sector": 1, "Profit Margin": 1, "_id": 0 })
cursor = cursor.sort({"Profit Margin": -1})
```

### 6. Renomeie o campo “Profit Margin” para apenas “profit”.

```javascript
db.stocks.update({"Profit Margin":{$exists:true}},{$rename:{"Profit Margin":"Profit"}},{multi: true}))
```

### 7. Agora liste apenas a empresa e seu respectivo resultado

```javascript
db.stocks.find({"Profit":{$exists: true}},{"Company":1,"Profit":1,"_id": 0}).sort({"Profit": -1})
```

### 8. Analise as ações. É uma bola de cristal na sua mão... Quais as três ações você investiria?

```javascript
db.stocks.find({}, {"Company": 1, "profit": 1}).sort({profit: -1})
```

### 9. Liste as ações agrupadas por setor

```javascript
db.stocks.aggregate([{$group: { _id: {"Sector": "$Sector"}}}])
```

## Exercício 3 - Fraude na Enron!

### 1. Liste as pessoas que enviaram e-mails (de forma distinta, ou seja, sem repetir). Quantas pessoas são?

```javascript
db.enron.distinct('sender').length
```

### 2. Contabilize quantos e-mails tem a palavra “fraud”

``` javascript
db.enron.find({"text": /fraud/}).count()
```
