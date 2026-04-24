### Bookstore Online Exercise

## Technology Choices

    For the project I selected the following technology stack:

    1. FastAPI / Python
        I have been a Node.js advocate for some time prior my work with DTT, but have been studying more about FastAPI, and seeing the benchmarks, it makes better sense, since the uphand Node.js had regarding speed are now being exceded by FastAPI. I used to work in a way that processes that required more computational power were buit into python microservices, and have the rest be served via node js (in backend). But I have been working more with FastAPI and am very conviced it is the best option currently for web development. My Python backend experience was centered in Django and Flask before this.

    2. Postgresql
        Basic relational database, with the capacity to support the concurrency that is expected.

    3. SqlAlchemy
        All models and db interactions are done using sqlalchemy.

    3. Alembic
        Per one of the requirements, in which management changes specifications constantly, being able to manage the database is of extreme importance. This includes progressive migrations and the ability to roll back to previous state with one command.

```batch
alembic upgrade head
alembic revision -m "add order_status initial data"
alembic downgrade -1
```
    4. Docker:
        The containers needed for deploying the application are executable using docker-compose

```batch
docker-compose up -d
```
