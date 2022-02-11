from enum import Enum
from fastapi import FastAPI
import re
import scraper

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from Edgar"}

@app.get("/api/aapl")
async def scrape():
    url = "https://stice05icedevsev001.z16.web.core.windows.net/"
    pageout = scraper.Scraper(str(url)).scrape_site()

    return {"result":pageout}
    