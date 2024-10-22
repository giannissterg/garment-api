from database_factory import DatabaseFactory
from pymongo import errors

class CollectionFactory:
    def __init__(self, db_factory: DatabaseFactory):
        self.db_factory = db_factory

    def create(self, db_name, collection_name, **collection_options):
        """
        Creates and returns a collection instance from the database created using DBFactory.
        Includes error handling and optional collection options.
        """
        db = self.db_factory.create(db_name)
        if db is not None:
            try:
                collection = db.get_collection(collection_name, **collection_options)
                return collection
            except errors.CollectionInvalid as coll_err:
                print(f"Invalid collection name or collection error: {coll_err}")
                return None
        else:
            print(f"Failed to create database {db_name}, cannot create collection.")
            return None
