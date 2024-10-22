import asyncio
import jsonlines
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from typing import Callable

from garment.garment import Garment
from usecases.pymongo_insert_usecase import PyMongoInsertManyUsecase

def readJsonLines(onGarmentRead: Callable[[dict], None]):
    with jsonlines.open("./assets/garments.jl") as garment_reader:
        for garment in garment_reader.iter(type=dict):
            onGarmentRead(garment)

# MongoDB setup
DB_NAME = "garment-db"
COLLECTION_NAME = "garmentsv6"

client: MongoClient = MongoClient("localhost", 27017)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

garment_validator = {
  "$jsonSchema": {
    "bsonType": "object",
    "required": [
      "gender",
      "product_id",
      "product_title",
      "product_description",
      "brand",
      "source",
      "product_categories",
      "url",
      "price",
      "discount",
      "currency_code",
      "stock",
      "stock_level",
      "additional_ids",
      "image_urls"
    ],
    "properties": {
      "gender": {
        "bsonType": "string",
        "description": "Gender field must be a string"
      },
      "product_id": {
        "bsonType": "string",
        "description": "Product ID must be a string"
      },
      "product_title": {
        "bsonType": "string",
        "description": "Product title must be a string"
      },
      "product_description": {
        "bsonType": "string",
        "description": "Product description must be a string"
      },
      "brand": {
        "bsonType": "string",
        "description": "Brand must be a string"
      },
      "source": {
        "bsonType": "string",
        "description": "Source must be a string"
      },
      "product_categories": {
        "bsonType": "array",
        "items": {
          "bsonType": "string"
        },
        "description": "Product categories must be an array of strings"
      },
      "url": {
        "bsonType": "string",
        "description": "URL must be a string"
      },
      "price": {
        "bsonType": "double",
        "description": "Price must be a double"
      },
      "discount": {
        "bsonType": "double",
        "description": "Discount must be a double"
      },
      "currency_code": {
        "bsonType": "string",
        "description": "Currency code must be a string"
      },
      "stock": {
        "bsonType": "int",
        "description": "Stock must be an integer"
      },
      "stock_level": {
        "bsonType": "int",
        "description": "Stock level must be an integer"
      },
      "additional_ids": {
        "bsonType": "array",
        "items": {
          "bsonType": "string"
        },
        "description": "Additional IDs must be an array of strings"
      },
      "image_urls": {
        "bsonType": "array",
        "items": {
          "bsonType": "string"
        },
        "description": "Image URLs must be an array of strings"
      },
      "position": {
        "bsonType": ["array", "null"],
        "items": {
          "bsonType": "string"
        },
        "description": "Position can be an array of strings or null"
      },
      "product_imgs_src": {
        "bsonType": ["array", "null"],
        "items": {
          "bsonType": "string"
        },
        "description": "Product image sources can be an array of strings or null"
      },
      "images": {
        "bsonType": ["array", "null"],
        "items": {
          "bsonType": "object",
          "required": ["url", "path", "s3_url", "s3_url_resized"],
          "properties": {
            "url": {
              "bsonType": "string",
              "description": "Image URL must be a string"
            },
            "path": {
              "bsonType": "string",
              "description": "Path must be a string"
            },
            "s3_url": {
              "bsonType": "string",
              "description": "S3 URL must be a string"
            },
            "s3_url_resized": {
              "bsonType": "string",
              "description": "Resized S3 URL must be a string"
            }
          }
        },
        "description": "Images must be an array of objects or null"
      }
    }
  }
}

db.command('collMod', COLLECTION_NAME, validator=garment_validator)

motor_client: AsyncIOMotorClient = AsyncIOMotorClient("localhost", 27017)
motor_db = client[DB_NAME]
motor_collection = db[COLLECTION_NAME]

def fetch_products() -> list:
    cursor = collection.find({"gender": "men"}).sort("_id")
    products = list(cursor)
    return products

lista: list[Garment] = []
def add_to_list(garment: dict):
    lista.append(Garment(**garment))


def log(item) -> str:
    return "Logging successful"

async def main():
    pMinsertManyUsecase = PyMongoInsertManyUsecase(collection)
    # motorInsertManyUsecase = LoggerUsecase(MotorInsertManyUsecase(motor_collection), logger=logger, logCallback=log)
    readJsonLines(add_to_list)
    pMinsertManyUsecase.execute(lista)
    # await motorInsertManyUsecase.execute(lista)
    # products = fetch_products()
    # print(products[:20])


if __name__ == "__main__":
    asyncio.run(main())