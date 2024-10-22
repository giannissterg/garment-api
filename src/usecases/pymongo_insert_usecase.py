from usecases.usecase import Usecase
from pymongo.collection import Collection

class PyMongoInsertUsecase[M](Usecase[M, bool]):
    def __init__(self, collection: Collection) -> None:
        self.collection = collection
    
    def execute(self, filter: M) -> bool:
        try:
            self.collection.insert_one(filter)
            return True
        except Exception:
            return False


class PyMongoInsertManyUsecase[M](Usecase[list[M], bool]):
    def __init__(self, collection: Collection) -> None:
        self.collection = collection
    
    def execute(self, filter: list[M]) -> bool:
        try:
            result = self.collection.insert_many(filter, ordered=False)
            print(result.inserted_ids)
            return True
        except Exception:
            return False

