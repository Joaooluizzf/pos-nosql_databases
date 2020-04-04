# pos-nosql_databases

#### Crie a tabela com 2 famílias de colunas
```
create 'italians', 'personal-data', 'professional-data'
```

#### Importe o arquivo via linha de comando

```
hbase shell /tmp/italians.txt
```

## Importe o arquivo via linha de comando, e agora execute as seguintes operações:

#### 1. Adicione mais 2 italianos mantendo adicionando informações como data de nascimento nas informações pessoais e um atributo de anos de experiência nas informações profissionais;

```
put 'italians', '9999', 'personal-data:name',  'Marcio Jasinski'
put 'italians', '9999', 'personal-data:city',  'Indaial(da Italia)'
put 'italians', '9999', 'personal-data:birthdate',  '01-01-1980'
put 'italians', '9999', 'professional-data:role',  'Research Coordinator'
put 'italians', '9999', 'professional-data:salary',  '12000'
put 'italians', '9999', 'professional-data:experience',  '30'


put 'italians', '9998', 'personal-data:name',  'Aurélio Faustino Hoppe'
put 'italians', '9998', 'personal-data:city',  'Ilhota(da Italia)'
put 'italians', '9998', 'personal-data:birthdate',  '01-01-1910'
put 'italians', '9998', 'professional-data:role',  'Programador'
put 'italians', '9998', 'professional-data:salary',  '6000'
put 'italians', '9998', 'professional-data:experience',  '28'
```


### 2. Adicione o controle de 5 versões na tabela de dados pessoais.

```
alter 'italians', NAME => 'personal-data', VERSIONS => 5
```


### 3. Faça 5 alterações em um dos italianos;

```
put 'italians', '12', 'personal-data:city',  'China'
put 'italians', '12', 'personal-data:city',  'Italia'
put 'italians', '12', 'personal-data:city',  'Espanha'
put 'italians', '12', 'professional-data:role',  'Hospedeiro'
put 'italians', '12', 'personal-data:city',  'Brasil'
```

### 4. Com o operador get, verifique como o HBase armazenou o histórico.

```
get 'italians', '11', {COLUMN=>'personal-data', VERSIONS=>5}
```

### 5. Utilize o scan para mostrar apenas o nome e profissão dos italianos.

```
scan 'italians', {COLUMNS=>['personal-data:name','professional-data:role']}
```

### 6. Apague um italiano com row id ímpar
```
deleteall 'italians', ['1', '3', '5','7','9','11']
```

### 7. Crie um contador de idade 55 para o italiano de row id 5

```
incr 'italians', 5, 'personal-data:age', 55
```

### 8. Incremente a idade do italiano em 1
```
incr 'italians', 5, 'personal-data:age', 1
```