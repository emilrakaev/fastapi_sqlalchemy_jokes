import asyncio

from src.db import database
from src.jokes.schemas import JokeIn
from src.models.joke import Joke


async def insert_into_db(joke: JokeIn):
    query = Joke.insert().values(type=joke.type,
                                 setup=joke.setup,
                                 punchline=joke.punchline)
    return await database.execute(query)


async def insert_jokes(data):
    joke_in_db = [insert_into_db(JokeIn(**i)) for i in data]
    await asyncio.gather(*joke_in_db)
