import logging
from starlette.middleware.base import BaseHTTPMiddleware
from usecases.pymongo_insert_usecase import PyMongoInsertUsecase

class GarmentCollectionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request.state.garment_collection = request.app.database["garmentv6"]
        garment_logger: logging.Logger = request.app.logger
        garment_logger.info(f"Injecting service into {request.url}")
        response = await call_next(request)
        return response


class GarmentGetUsecaseMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        print("GetMiddleware")
        get_usecase = PyMongoInsertUsecase(request.state.garment_collection)
        request.state.garments_get_usecase = get_usecase
        prods = request.state.garment_collection.find({}).sort("_id")
        products = list(prods)
        print(products[:10])
        get_usecase.execute({"id": 2, "name": "fsg"})
        response = await call_next(request)
        return response
