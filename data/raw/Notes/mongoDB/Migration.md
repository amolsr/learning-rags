### Exporting Data From Mongodb Collection
```
mongoexport --uri "<URL>" --collection <CollectionName> --type=csv --out text.csv --fields "<FieldsName>"
```

### Importing Data Into Mongodb Collection
```
mongoimport --uri "<URL>" --collection <CollectionName> --type=csv --file text.csv --headerline
```

### M001

#### BSON
```
mongodump --uri "mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/sample_supplies"
  
mongorestore --uri "mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/sample_supplies"  --drop dump
```
#### JSON
```
mongoexport --uri="mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/sample_supplies" --collection=sales --out=sales.json

mongoimport --uri="mongodb+srv://<your username>:<your password>@<your cluster>.mongodb.net/sample_supplies" --drop sales.json
```
