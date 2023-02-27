import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from databases import Database

load_dotenv()
DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER', 'postgres')}:{os.getenv('POSTGRES_PASSWORD', 'postgres')}@postgres/{os.getenv('POSTGRES_DB', 'postgres')}"

engine = create_engine(DATABASE_URL)

database = Database(DATABASE_URL)
