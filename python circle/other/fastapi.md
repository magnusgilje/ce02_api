# initialising
In terminal

`python -m venv .`

after run, then run

`.\scripts\activate`

create a
populate the main.py file with:

```python
from fastapi import FastAPI

app= FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from Circle"}
```
pip install fastapi
pip install uvicorn

uvicorn main:app --reload

in terminal an ip will appear, e.g `127.0.0.1:8000`

in chrome put in `127.0.0.1:8000`

## Swagger
append url with 

`/docs`

## Redoc
append url with

`/redoc`