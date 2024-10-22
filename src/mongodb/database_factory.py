from typing import Optional
from pymongo import errors
from pymongo.database import Database

from pymongo_factory import PyMongoFactory


class DatabaseFactory:
    def __init__(self, mongo_factory: PyMongoFactory):
        self.mongo_factory = mongo_factory

    def create(self, database_name) -> Optional[Database]:
        """
        Creates and returns a database instance with error handling and optional database options.
        """
        client = self.mongo_factory.create()
        if client:
            try:
                db = client.get_database(database_name)
                return db
            except errors.InvalidName as inv_name_err:
                print(f"Invalid database name: {inv_name_err}")
                return None
        else:
            print("Failed to create MongoClient, cannot create database.")
            return None
