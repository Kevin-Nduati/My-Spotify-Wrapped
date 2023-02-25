from fastapi import FastAPI
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

@app.get("/callback")
async def authorize():
    return "This is my callback page"