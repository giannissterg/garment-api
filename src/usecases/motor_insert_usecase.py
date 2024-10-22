from usecases.usecase import Usecase
from motor.motor_asyncio import AsyncIOMotorCollection


class MotorInsertUsecase[M](Usecase[M, bool]):
    def __init__(self, collection: AsyncIOMotorCollection) -> None:
        self.collection = collection
    
    def execute(self, data: M) -> bool:
        try:
            self.collection.insert_one(data)
            return True
        except Exception:
            return False


class MotorInsertManyUsecase[M](Usecase[list[M], bool]):
    def __init__(self, collection: AsyncIOMotorCollection) -> None:
        self.collection = collection
    
    async def execute(self, data: list[M]) -> bool:
        try:
            result = await self.collection.insert_many(data, ordered=False)
            print(result.inserted_ids)
            return True
        except Exception:
            return False

