## friendship-test

Friendship Test can be used to create interesting quizzes and then share link to others for attempting and see the results.

### Install
Run the compose stack by:

`docker-compose up -d`

### Seed DB
Once the services are running:

Run `docker exec -it ft-backend make db_seed`

This feeds the db with questions and also creates django admin user.
- Go to http://localhost:8080/admin
- Login with username: `admin` and password `admin`
- FE will be running at http://localhost:3000/

#### Design decisions / assumptions
- It's a read-heavy system. Creation of new quizzes will be less compared to the access to the quizzes (1 user sends link to multiple friends/followers)
- Once a quiz is created, the collection of questions inside it won't be changed
- Based on the two above assumptions, the `Quiz` model holds questions/answers in itself as JSON columns, instead of linking to the actual tables. This creates a data redundancy 
but the upside is that we won't have to traverse relationships to present a quiz. Quiz retreival and checking will be quick. Quiz is a user view (optimized for quick retrieval)
- If we want some analytics on the created quiz,e.g., which questions are present in which quizes etc then storage in JSON columns is not good.
- Sharable links should not be guessable (shouldn't be auto increment / PK based etc). But they shouldn't be too long and complex, easy to type if you have to.
