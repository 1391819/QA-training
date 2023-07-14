# SQL Practice Stuff

`\! cls` -> useful 

## Basic inspection

```sql
SHOW DATABASES;
```

```sql
SHOW TABLES;
```

```sql
DESCRIBE genres;
```

```sql
DESCRIBE genres_movies;
```

```sql
DESCRIBE movies;
```

```sql
DESCRIBE occupations;
```

```sql
DESCRIBE ratings;
```

```sql
DESCRIBE users;
```

## Select queries

```sql
SELECT * FROM genres;
```

```sql
SELECT * from movies LIMIT 20;
```

```sql
SELECT * FROM occupations;
```

```sql
SELECT COUNT(*) FROM ratings;
```

```sql
SELECT COUNT(*) FROM users;
```

```sql
SELECT title FROM movies ORDER BY release_date ASC LIMIT 10;
```

```sql
SELECT title FROM movies ORDER BY release_date DESC LIMIT 10;
```


## Bit more advanced

1. Get a random id for now, even though we could search for a particular name as well (`WHERE title = '%aaa%'`)

    ```sql
    SELECT * FROM movies WHERE id = 1;
    ``` 

2. See the categories associated with id=1 movie in genres_movies table

    ```sql
    SELECT * FROM genres_movies WHERE movie_id = 1;
    ```

3. Going for movie_id = 1 (Toy Story genres)

    ```sql
    SELECT t3.title, t2.name
    FROM genres_movies AS t1 
    INNER JOIN genres AS t2 
    ON t1.genre_id = t2.id 
    INNER JOIN movies AS t3 
    ON t1.movie_id = t3.id 
    WHERE t1.movie_id = 1;
    ```
