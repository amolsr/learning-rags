Authenticate as root user:
```
mongo admin -u root -p root123
```
Create security officer:
```
db.createUser(
  { user: "security_officer",
    pwd: "h3ll0th3r3",
    roles: [ { db: "admin", role: "userAdmin" } ]
  }
)
```
Create database administrator:
```
db.createUser(
  { user: "dba",
    pwd: "c1lynd3rs",
    roles: [ { db: "admin", role: "dbAdmin" } ]
  }
)
```
Grant role to user:
```
db.grantRolesToUser( "dba",  [ { db: "playground", role: "dbOwner"  } ] )
```
Show role privileges:
```
db.runCommand( { rolesInfo: { role: "dbOwner", db: "playground" }, showPrivileges: true} )
```
