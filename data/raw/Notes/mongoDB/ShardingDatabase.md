Show collections in m103 database:
```
use m103
show collections
```
Enable sharding on the m103 database:
```
sh.enableSharding("m103")
```
Find one document from the products collection, to help us choose a shard key:
```
db.products.findOne()
```
Create an index on sku:
```
db.products.createIndex( { "sku" : 1 } )
```
Shard the products collection on sku:
```
sh.shardCollection("m103.products", {"sku" : 1 } )
```
Checking the status of the sharded cluster:
```
sh.status()
```
