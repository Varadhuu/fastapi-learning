from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import time
import asyncio

app = FastAPI()

JOKE_URL = "https://official-joke-api.appspot.com/random_joke"

@app.get("/jokes/sync")
def get_joke_sync():
    start = time.time()
    jokes = []
    with httpx.Client() as client:
        for _ in range(10):
            response = httpx.get(JOKE_URL)
            data = response.json()
            jokes.append(data)
    elapsed = time.time() - start

    return {
        "mode" : "sync",
        "elapsed_time" : elapsed,
        "jokes" : jokes
    }


@app.get("/jokes/async")
async def get_joke_async():
    start = time.time()
    jokes = []
    async with httpx.AsyncClient() as client:
        task = [client.get(JOKE_URL) for _ in range(10)]
        responses = await asyncio.gather(*task)
        for i in responses:
            data = i.json()
            jokes.append(data)
    elapsed = time.time() - start

    return {
        "mode" : "async",
        "elapsed_time" : elapsed,
        "jokes" : jokes
    }