import contextlib
from starlette.applications import Starlette
from starlette.config import Config
from starlette.schemas import SchemaGenerator
from starlette.responses import JSONResponse, PlainTextResponse
from starlette.routing import Route, Mount
import uvicorn

from pymongo.database_factory import DatabaseFactory
from pymongo.pymongo_factory import PyMongoFactory

config = Config(".env")
DATABASE_URL = config("DATABASE_URL")

schemas = SchemaGenerator(
    {"openapi": "3.0.0", "info": {"title": "Example API", "version": "1.0"}}
)


async def get_garments(request):
    """
    responses:
      200:
        description: A list of users.
        examples:
          [{"username": "tom"}, {"username": "lucy"}]
    """
    return PlainTextResponse("A list of garments")
    raise NotImplementedError()


async def create_garment(request):
    """
    responses:
      200:
        description: A user.
        examples:
          {"username": "tom"}
    """
    return PlainTextResponse("Garment created")
    raise NotImplementedError()


async def get_garment(request):
    """
    responses:
      200:
        description: A user.
        examples:
          {"username": "tom"}
    """
    return JSONResponse("Got a garment")
    raise NotImplementedError()


async def update_garment(request):
    """
    responses:
      200:
        description: A user.
        examples:
          {"username": "tom"}
    """
    return PlainTextResponse("A garment was updated")


async def delete_garment(request):
    """
    responses:
      200:
        description: A user.
        examples:
          {"username": "tom"}
    """
    return PlainTextResponse("A garment got deleted")


async def openapi_schema(request):
    return schemas.OpenAPIResponse(request=request)


async def error(request):
    """
    An example error. Switch the `debug` setting to see either tracebacks or 500 pages.
    """
    raise RuntimeError("Oh no")


garment_routes = Mount(
    "/{garment_id}",
    routes=[
        Route("/", endpoint=get_garment, methods=["GET"]),
        Route("/", endpoint=update_garment, methods=["PUT"]),
        Route("/", endpoint=delete_garment, methods=["DELETE"]),
    ],
)

garment_list_routes = Mount(
    "/garments",
    routes=[
        Route("/", endpoint=get_garments, methods=["GET"]),
        Route("/", endpoint=create_garment, methods=["POST"]),
        garment_routes,
    ],
)

routes = [
    Route("/error", endpoint=error),
    garment_list_routes,
    Route("/schema", endpoint=openapi_schema, include_in_schema=False),
]

exception_handlers = {500: error}


@contextlib.asynccontextmanager
async def lifespan(app):
    print("Starting connection to database...")
    factory = PyMongoFactory()
    app.mongodb_client = factory.create()
    app.database = app.mongodb_client["j"]
    yield
    app.mongodb_client.close()
    print("Database connection closed.")


app = Starlette(
    debug=True,
    routes=routes,
    exception_handlers=exception_handlers,
    lifespan=lifespan,
)

if __name__ == "__main__":
    print(DATABASE_URL)
    uvicorn.run(app, host="localhost", port=8080)
