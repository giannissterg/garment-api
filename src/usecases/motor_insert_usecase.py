from usecases.usecase import AsyncUsecase
from motor.motor_asyncio import AsyncIOMotorCollection


class MotorInsertUsecase[M](AsyncUsecase[M, bool]):
    def __init__(self, collection: AsyncIOMotorCollection) -> None:
        self.collection = collection
    
    async def execute(self, filter: M) -> bool:
        try:
            await self.collection.insert_one(filter)
            return True
        except Exception:
            return False


class MotorInsertManyUsecase[M](AsyncUsecase[list[M], bool]):
    def __init__(self, collection: AsyncIOMotorCollection) -> None:
        self.collection = collection
    
    async def execute(self, filter: list[M]) -> bool:
        try:
            result = await self.collection.insert_many(filter, ordered=False)
            print(result.inserted_ids)
            return True
        except Exception:
            return False

