from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app= FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/edgar/top100")
async def top_100():
    return{"TBA":"TBA"}

@app.get("/edgar/top100/{count}")
async def top_100_n(count:int):
    return {"companies": []}

@app.get("/edgar/company/{index}")
async def top_100_n(index:int):
    return {"companies": "<html><body><h1>This is the Title for {index}</h1></body></html>"}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_item(user_id: int):
    return {"user_id": user_id}

@app.get("/models/{model_name}")
async def get_models(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return{"model_name": model_name, "message": "Deep learning"}

    if model_name == ModelName.lenet:
        return{"model_name": model_name, "message":"LeCNN"}
    
    if model_name == ModelName.resnet:
        return{"model_name": model_name, "message":"Residuals"}
