FROM python:3.11.2-buster
# RUN apt-get update && apt install -y curl
# RUN curl -sSL https://install.python-poetry.org | python
# ENV PATH="${PATH}:/root/.local/bin"
RUN pip install poetry
RUN poetry config virtualenvs.in-project true
WORKDIR /app
COPY . .
RUN rm -rf webapp
RUN rm -rf .env
RUN mv worker/.env_container .env
RUN rm -rf alembic.ini
RUN mv worker/alembic_container.ini alembic.ini
RUN poetry install
CMD ["celery", "-A", "tasks", "worker", "--loglevel=info"]
