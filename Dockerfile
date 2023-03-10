FROM python:3.10-slim-buster as py-build

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
    POETRY_VERSION=1.3.2 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'


RUN apt-get update \
  && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
    gettext \
    git \
    libpq-dev \
    wget \
  # Cleaning cache:
  && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
  && pip install "poetry==$POETRY_VERSION" && poetry --version

# set work directory
WORKDIR /code
COPY pyproject.toml poetry.lock /code/

# Install dependencies:
RUN poetry install --no-root
# copy project
COPY . /code

#CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]