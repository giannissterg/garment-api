from usecases.usecase import Usecase

class PyMongoInsertUsecase[M](Usecase[M, bool]):
    def __init__(self, collection) -> None:
        self.collection = collection
    
    def execute(self, data: M) -> bool:
        try:
            self.collection.insert_one(data)
            return True
        except Exception:
            return False


class PyMongoInsertManyUsecase[M](Usecase[list[M], bool]):
    def __init__(self, collection) -> None:
        self.collection = collection
    
    def execute(self, data: list[M]) -> bool:
        try:
            result = self.collection.insert_many(data, ordered=False)
            print(result.inserted_ids)
            return True
        except Exception:
            return False

