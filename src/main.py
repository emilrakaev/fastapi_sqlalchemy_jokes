from typing import List

from fastapi import FastAPI, status, Depends

from src.db import database
from src.jokes import schemas
from src.jokes import use_cases
from src.models.joke import Joke
from src.jokes import deps

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post('/', response_model=List[schemas.JokeIn], status_code=status.HTTP_201_CREATED)
async def load_jokes(joke_ap: list = Depends(deps.get_jokes_from_api)):
    await use_cases.insert_jokes(joke_ap)
    return joke_ap


@app.get("/jokes/", response_model=List[schemas.Joke], status_code=status.HTTP_200_OK)
async def resd_jokes():
    query = Joke.select()
    return await database.fetch_all(query)


@app.post('/create_joke/', response_model=schemas.Joke, status_code=status.HTTP_201_CREATED)
async def create_joke(joke_params: schemas.JokeIn):
    query = Joke.insert().values(type=joke_params.type, setup=joke_params.setup, punchline=joke_params.punchline)
    last_record_id = await database.execute(query)
    return {**joke_params.dict(), "id": last_record_id}
