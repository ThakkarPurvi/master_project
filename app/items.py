from main import *

from fastapi import APIRouter
from pymongo import MongoClient
from fastapi.encoders import jsonable_encoder
import os

router = APIRouter()

# MongoDB Connection
mongo_client = MongoClient(os.environ.get('PRIMARY_CONNECTION_STRING'))
db = mongo_client["master-db"]
collection = db["master-db"]

@router.get("/test")
async def testing():
    return {"Master": "Project"}

@router.get("/insert")
async def test_insert():
    mongo_db = mongo_client['master-db']
    data = mongo_db.tasks.insert_one({"Fruit": "Apple"})
    return jsonable_encoder(data)