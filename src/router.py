import contextlib
from logging import StreamHandler
import logging
import sys
from starlette.applications import Starlette
from starlette.config import Config
from starlette.middleware import Middleware
from starlette.schemas import SchemaGenerator
from starlette.routing import Route, Mount
import uvicorn

from garment_collection_middleware import (
    GarmentCollectionMiddleware,
    GarmentGetUsecaseMiddleware,
)
from garment_endpoint import GarmentEndpoint
from garment_list_endpoint import GarmentListEndpoint
from log.logger_config import LoggerConfig
from log.py_logger_factory import PyLoggerFactory
from mongodb.pymongo_factory import PyMongoFactory

config = Config(".env")
DATABASE_HOST = config("MONGO_DATABASE_HOST")
DATABASE_PORT = config("MONGO_DATABASE_PORT")
SERVER_HOST = config("GARMENT_SERVER_HOST")
SERVER_PORT = int(config("GARMENT_SERVER_PORT"))

schemas = SchemaGenerator(
    {"openapi": "3.0.0", "info": {"title": "Example API", "version": "1.0"}}
)


async def openapi_schema(request):
    return schemas.OpenAPIResponse(request=request)


def error(request, exception):
    """
    An example error. Switch the `debug` setting to see either tracebacks or 500 pages.
    """
    raise RuntimeError("Oh no")


garment_list_routes = Mount(
    "/garments",
    routes=[
        Route(
            "/",
            endpoint=GarmentListEndpoint,
            middleware=[Middleware(GarmentGetUsecaseMiddleware)],
        ),
        Route("/{garment_id}", endpoint=GarmentEndpoint),
    ],
    middleware=[Middleware(GarmentCollectionMiddleware)],
)

routes = [
    Route("/error", endpoint=error),
    garment_list_routes,
    Route("/schema", endpoint=openapi_schema, include_in_schema=False),
]

exception_handlers = {500: error}


mongo_factory = PyMongoFactory(uri=f"mongodb://{DATABASE_HOST}:{DATABASE_PORT}/")
logger_factory = PyLoggerFactory()
logger_config = LoggerConfig(
    "GARMENT",
    handlers=[StreamHandler()],
    formatter=logging.Formatter("[%(name)s][%(levelname)s] %(message)s (%(asctime)s)"),
)


@contextlib.asynccontextmanager
async def lifespan(app):
    logger = logger_factory.create_logger(logger_config)
    logger.info(f"Starting connection to database: {DATABASE_HOST}")
    mongo_client = mongo_factory.create()
    if mongo_client is None: 
        logger.error("Could not establish a conenction with Mongo")
        sys.exit(1)
    app.logger = logger
    app.database = mongo_client["garment-db"]
    yield
    mongo_factory.destroy()
    logger.info("Database connection closed.")


app = Starlette(
    debug=True,
    routes=routes,
    exception_handlers=exception_handlers,
    lifespan=lifespan,
)

if __name__ == "__main__":
    uvicorn.run(app, host=SERVER_HOST, port=SERVER_PORT)
