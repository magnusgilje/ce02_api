from fastapi import FastAPI
from fastapi.logger import logger
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from Random"}

@app.get("/random")
async def random_number():
    rand = random.randint(1,100)
    return {"random": rand}

@app.get("/random_numbers")
async def random_numbers():
    numbers = [random.randint(1,100) for i in range (0,50)]
    return {"random": numbers}

@app.get("/status")
async def status():
    if random.randint(1,100)>90:
        return {"status": "starting"}
    
    if random.randint(1,100)>98:
        return {"status": "Error"}
    
    return {"status": "OK"}