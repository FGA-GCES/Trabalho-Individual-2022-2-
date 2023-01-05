# Playground

### Instaling Requirements

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Running

```
python src/main.py
```

### Testing

```
pytest --cov
```

### Metabase

The metabase will help us visualize and monitor data processing, feature engineering and model monitoring, accompanying us throughout the cycle.

| Keywords  | Description |
|-----------|-------------|
|   CSV     | A CSV file is a plain text file that stores table and spreadsheet information. CSV files can be easily imported and exported using programs that store data in tables.|
| Collection| A collection is a grouping of MongoDB documents. Documents within a collection can have different fields. A collection is the equivalent of a table in a relational database system.|
|  Database | A database stores one or more collections of documents.|
| Mongo| It is a NoSQL database developed by MongoDB Inc. MongoDB database is built to store a huge amount of data and also perform fast.|



**Connect the database to the metabase**

- step 1: Open localhost:3000
- step 2: Click Admin setting
- step 3: Click Database
- step 4: Add database authentication data


**Exemple mongo connect metabase**
|  metabase  | credential  |
|------------|-------------|
|    host    |  mongo  |
|dabase_name | use the name you define in make migrate|
|    user    |   lappis    |
|  password  |   lappis    |

