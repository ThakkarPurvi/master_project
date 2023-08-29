from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.encoders import jsonable_encoder
import os
import uvicorn

app = FastAPI()

# MongoDB Connection
mongo_client = MongoClient(os.environ.get('PRIMARY_CONNECTION_STRING'))
db = mongo_client["master-db"]
collection = db["master-db"]

@app.get("/")
async def home():
    return {"Home"}

if __name__ == "__main__":
    uvicorn.run(app, port=5000, log_level="info")