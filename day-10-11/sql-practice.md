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

    This can be further expanded and joined to other tables (e.g., ratings)

## Bit more practice?

```sql
-- use world.sql 
USE world;

-- Counting number of countries in Asia
SELECT Count(Name) 
FROM country 
WHERE Continent="Asia";


-- Returning country with the highest GNP 
SELECT Name, MAX(GNP) AS MAX_GNP 
FROM country 
GROUP BY Name 
ORDER BY MAX_GNP DESC 
LIMIT 1;
```

```sql
-- Returning Continent and average GNP for each one
-- Group the data by continent, calculate average GNP for each group
-- and order the results in descending order based on the average GNP
SELECT Continent, AVG(GNP) AS Avg_GNP
FROM country 
GROUP BY Continent
ORDER BY Avg_GNP DESC;
```

```sql
DESC city;
-- Returning city with the highest population
SELECT Name, MAX(Population) as highest_population
FROM city 
GROUP BY Name
ORDER BY highest_population DESC
LIMIT 1;
```

```sql
-- Returning top 10 countries with the highest population (sum of all cities)
SELECT countryCode, SUM(Population) as total_population
FROM city 
GROUP BY countryCode
ORDER BY total_population DESC
LIMIT 10;
```
