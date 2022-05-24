import time
import asyncio
from fastapi import FastAPI


app = FastAPI()

@app.get("/sync-loadtest")
def synchronous_route():
    time.sleep(1)

    # Grab some amount of memory
    bytearray(512000000)
    return {"message": "Synchronous Hello World!"}


@app.get("/async-loadtest")
async def asynchronous_route():
    await asyncio.sleep(1)
    start_time= time.time()
    # Emulate large objects in memory
    bytearray(512000000)
    end_time= time.time()
    print(f'time to allocate bytearray {end_time - start_time}')
    return {"message": "Asynchronous Hello World!"}
