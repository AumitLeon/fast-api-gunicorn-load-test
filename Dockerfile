FROM python:3.10.0

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | \
  POETRY_HOME=/opt/poetry python - && \
  cd /usr/local/bin && \
  ln -s /opt/poetry/bin/poetry


WORKDIR /src

# Maintain docker layer cache since our dependencies won't change often.
COPY ./pyproject.toml ./poetry.lock /src/

# Install dependencies.
RUN poetry install

# Copy over the main fast api application.
COPY ./app/ /src/app/

# Copy over the gunicorn configuration file.
COPY ./gunicorn_conf.py /src/

CMD ["poetry", "run", "gunicorn", "-c", "python:gunicorn_conf", "app.main:app", "--access-logfile",  "-", "-b", "0.0.0.0:80"]
