FROM python:3.12-slim-bookworm

# Combine environment variable declarations into a single ENV statement
ENV TZ=Europe/Amsterdam \
    SHELL=/bin/bash \
    POETRY_VERSION=1.8.2

# Combine installation commands and cleanup
RUN apt-get update && apt-get upgrade -y
RUN apt-get install graphviz -y

# Install poetry
RUN python -m pip install "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.in-project true
