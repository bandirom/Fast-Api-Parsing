# Fast-Api-Parsing

## Github clone:

    git clone https://github.com/bandirom/Fast-Api-Parsing.git .
    
## Build docker
    docker-compose up -d --build

### Server: [localhost:8080](http://localhost:8080)

## Logs: docker-compose logs -f
## Using logs, you can check how many links parsed and how many left

### Access to DB:

    docker-compose exec db psql --username=spd_ukraine --dbname=spd_ukraine
    
### SQL:

```sql
    SELECT COUNT(*) FROM links;
    SELECT title, url FROM links WHERE lower(context) SIMILAR TO 'google' LIMIT 10;
```
    