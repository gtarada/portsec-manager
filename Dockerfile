# TODO change to -slim image
FROM python:3.9
# TODO add nginx and change to 80
EXPOSE 5000
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME="/opt/poetry"

WORKDIR /app

# RUN apt-get update && \
#     apt-get install --no-install-recommends -y curl && \
#     apt-get clean && rm -rf /var/lib/apt/lists/*

RUN curl -sSL -o install-poetry.py https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py && \
    python install-poetry.py -y

# Copy using poetry.lock* in case it doesn't exist yet
COPY pyproject.toml poetry.lock* /app/

RUN $POETRY_HOME/bin/poetry config experimental.new-installer false && \
    $POETRY_HOME/bin/poetry install --no-interaction --no-root --no-dev

COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "web.webapp:app"]
