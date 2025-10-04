#### Running Bash into Docker Container

```bash
docker exec -it <ContainerName/ContainerID> bash
```

#### Copy File into Docker Container

```bash
docker cp <file-path> <ContainerName>:<destinationPath>
```

#### Docker Postgres Setup

1. Open cmd and pull the Docker Postgres image using the command:  
   ```bash
   docker pull postgres
   ```

2. Wait for it to download.

3. Run the container using the command:  
   ```bash
   docker run --name postgresContainer -e POSTGRES_PASSWORD=123 -d -p 5432:5432 postgres
   ```

4. Verify if the container is running using the command:  
   ```bash
   docker ps
   ```

5. You can execute psql commands using the command:  
   ```bash
   docker exec -it postgresContainer psql -U postgres
   ```

6. Once psql opens, use this command to create a test database:  
   ```sql
   CREATE DATABASE test_db;
   ```

7. More Docker resources:  
   [Postgres Docker Hub](https://hub.docker.com/_/postgres)

#### Docker MySQL Setup

1. Open cmd and pull the Docker MySQL image using the command:  
   ```bash
   docker pull mysql
   ```

2. Wait for it to download.

3. Run the container using the command:  
   ```bash
   docker run --name mysqlContainer -e MYSQL_ROOT_PASSWORD=123 -d -p 3306:3306 mysql
   ```

4. Verify if the container is running using the command:  
   ```bash
   docker ps
   ```

5. You can execute MySQL commands using the command:  
   ```bash
   docker exec -it mysqlContainer mysql --user=root --password
   ```

6. Enter the password.

7. Once MySQL opens, use this command to create a test database:  
   ```sql
   CREATE DATABASE test_db;
   ```

8. More Docker resources:  
   [MySQL Docker Hub](https://hub.docker.com/_/mysql)
