# Challenges using the movielens db

## Intro

You will need to use the movielens database to solve these problems.

## Tasks

1. List the titles and release dates of movies released between 1983-1993 in reverse chronological order.
   
   ```sql
   SELECT title, release_date 
   FROM movies
   WHERE release_date BETWEEN '1983-01-01' AND '1993-01-01'
   ORDER BY release_date ASC
   ```

2. Without using LIMIT, list the titles of the movies with the lowest average rating.
   
   ```sql
   SELECT title, AVG(rating) as average_rating
   FROM movies
   LEFT JOIN ratings 
   ON movies.id = ratings.movie_id
   GROUP BY title
   ORDER BY average_rating;
   ```

3. List the unique records for Sci-Fi movies where male 24-year-old students have given 5-star ratings.
   
   ```sql
   -- Getting Sci-fi ID - 15
   SELECT id
   FROM genres
   WHERE name = "Sci-Fi";

   -- Getting student ID - 19
   SELECT id
   FROM occupations 
   WHERE name = "Student";

   -- Getting 24 yo males
   SELECT id 
   FROM users
   WHERE age = 24 AND gender = "M";

   -- Combining 2 and 3 to get right users id
   SELECT users.id
   FROM users 
   LEFT JOIN occupations 
   ON users.occupation_id = occupations.id 
   WHERE users.age = 24 AND users.gender = "M" AND occupations.name = "Student";
   
   -- Now we have all the 24yo males who are students who could have left a review (subtable)

   -- We work on a basis for the final query - movies which have 5 ratings
   SELECT id, movie_id
   FROM ratings
   WHERE ratings.rating = 5;

   -- Keep working on it -> with this, we have 
   -- all the movies that a male 24yo student rated as 5 stars
   SELECT ratings.movie_id
   FROM (
    SELECT users.id
    FROM users 
    LEFT JOIN occupations 
    ON users.occupation_id = occupations.id 
    WHERE users.age = 24 AND users.gender = "M" AND occupations.name = "Student"
   ) AS valid_users
   LEFT JOIN ratings
   ON ratings.user_id = valid_users.id
   WHERE ratings.rating = 5
   LIMIT 10;
   
   -- Now my head is just spinning, we need to add movies, genres_movies, and genres? + adding distinct for unique records
   SELECT DISTINCT movies.id AS movie_id, movies.title, genres.name AS genre, ratings.rating, valid_users.age, 
   valid_users.gender, valid_users.occupation_name
   FROM (
    SELECT users.id, users.age, users.gender, occupations.name AS occupation_name
    FROM users 
    LEFT JOIN occupations 
    ON users.occupation_id = occupations.id 
    WHERE users.age = 24 AND users.gender = "M" AND occupations.name = "Student"
   ) AS valid_users
   LEFT JOIN ratings
   ON ratings.user_id = valid_users.id
   LEFT JOIN movies
   ON movies.id = ratings.movie_id
   LEFT JOIN genres_movies 
   ON movies.id = genres_movies.movie_id
   LEFT JOIN genres
   ON genres_movies.genre_id = genres.id
   WHERE ratings.rating = 5 AND genres.name = "Sci-Fi";
   ```

4. List the unique titles of each of the movies released on the most popular release day.
   
   ```sql

   ```

5. Find the total number of movies in each genre; list the results in ascending numeric order.
   
   ```sql

   ```
