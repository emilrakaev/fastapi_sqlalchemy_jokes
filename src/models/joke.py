import sqlalchemy

from src.db import engine

metadata = sqlalchemy.MetaData()

Joke = sqlalchemy.Table(
    "joke",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("type", sqlalchemy.String),
    sqlalchemy.Column("setup", sqlalchemy.String),
    sqlalchemy.Column("punchline", sqlalchemy.String),
)

metadata.create_all(engine)
