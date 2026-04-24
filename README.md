### Bookstore Online Exercise

## Technology Choices


For the project I selected the following technology stack:

1. FastAPI / Python / Poetry
    I have been a Node.js advocate for some time prior my work with DTT, but have been studying more about FastAPI, and seeing the benchmarks, it makes better sense, since the uphand Node.js had regarding speed are now being exceded by FastAPI. I used to work in a way that processes that required more computational power were buit into python microservices, and have the rest be served via node js (in backend). But I have been working more with FastAPI and am very conviced it is the best option currently for web development. My Python backend experience was centered in Django and Flask before this. I am using Poetry for dependency and script management.

2. Postgresql
        Basic relational database, with the capacity to support the concurrency that is expected.

3. SqlAlchemy
        All models and db interactions are done using sqlalchemy.

4. Alembic
        Per one of the requirements, in which management changes specifications constantly, being able to manage the database is of extreme importance. This includes progressive migrations and the ability to roll back to previous state with one command.


alembic upgrade head
alembic revision -m "add order_status initial data"
alembic downgrade -1

5. Docker:
        The containers needed for deploying the application are executable using docker-compose


docker-compose up -d

    Docker will then initialize the required (postgres, rabbitmq) containers to run the application,

6. Celery:
        I am including the possibility to delegate the order process, specially the order definition, which requires the most work, to one or multiple workers using Celery and Rabbitmq as a broker. This will distribute the workload between different nodes or servers, and the requirement of scalability can be met.

