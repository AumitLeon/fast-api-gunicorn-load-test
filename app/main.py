import time
import asyncio
from fastapi import FastAPI


app = FastAPI()

@app.get("/sync-loadtest")
def synchronous_route():
    time.sleep(1)
    return {"message": "Synchronous Hello World!"}


@app.get("/async-loadtest")
def synchronous_route():
    asyncio.sleep(1)
    return {"message": "AsynchronousHello World!"}
