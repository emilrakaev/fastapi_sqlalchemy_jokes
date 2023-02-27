import asyncio
import os

import aiohttp
from dotenv import load_dotenv

load_dotenv()


async def custom_request(session):
    async with session.get(os.getenv('URL')) as response:
        return await response.json()


async def get_jokes_from_api():
    async with aiohttp.ClientSession() as session:
        tasks = [custom_request(session) for i in range(3)]
        return await asyncio.gather(*tasks)