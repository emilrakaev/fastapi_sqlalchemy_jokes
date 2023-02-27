import os
from dotenv import load_dotenv
from sqlalchemy import (Column, Integer, String, Table, create_engine, MetaData)
from databases import Database

load_dotenv()
DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER', 'postgres')}:{os.getenv('POSTGRES_PASSWORD', 'postgres')}@postgres/{os.getenv('POSTGRES_DB', 'postgres')}"

engine = create_engine(DATABASE_URL)
metadata = MetaData()
Joke = Table(
    "joke",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("type", String),
    Column("setup", String),
    Column("punchline", String)
)

database = Database(DATABASE_URL)
