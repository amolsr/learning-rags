#### Import data from csv to Table.

```
COPY search_table
FROM '/usr/input.csv'
DELIMITER ','
CSV HEADER;
```

#### Import data from csv to table when less privilege is granted to user

```
/COPY search_table
FROM '/usr/input.csv'
DELIMITER ','
CSV HEADER;
```
