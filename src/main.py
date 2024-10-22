import asyncio
import logging
import jsonlines
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from typing import Callable

from usecases.logger_usecase import LoggerUsecase
from usecases.motor_insert_usecase import MotorInsertManyUsecase
from usecases.pymongo_insert_usecase import PyMongoInsertManyUsecase

def readJsonLines(onGarmentRead: Callable[[dict], None]):
    with jsonlines.open("./assets/garments.jl") as garment_reader:
        for garment in garment_reader.iter(type=dict):
            onGarmentRead(garment)


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("GARMENT")

# MongoDB setup
DB_NAME = "garment-db"
COLLECTION_NAME = "garmentsv5"

client: MongoClient = MongoClient("localhost", 27017)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

motor_client = AsyncIOMotorClient("localhost", 27017)
motor_db = client[DB_NAME]
motor_collection = db[COLLECTION_NAME]


def fetch_products(last_id=None) -> list:
    cursor = collection.find({"gender": "men"}).sort("_id")
    products = list(cursor)
    return products

lista = []
def add_to_list(garment: dict):
    lista.append(garment)


def log(item) -> str:
    return "Logging successful"

async def main():
    # pMinsertManyUsecase = PyMongoInsertManyUsecase(collection)
    motorInsertManyUsecase = LoggerUsecase(MotorInsertManyUsecase(motor_collection), logger=logger, logCallback=log)
    readJsonLines(add_to_list)
    # pMinsertManyUsecase.execute(lista)
    await motorInsertManyUsecase.execute(lista)
    # products = fetch_products()
    # print(products[:20])


if __name__ == "__main__":
    asyncio.run(main())