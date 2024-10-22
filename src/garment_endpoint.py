from starlette.responses import PlainTextResponse, JSONResponse
from starlette.endpoints import HTTPEndpoint

class GarmentEndpoint(HTTPEndpoint):
    async def get(self, request):
        """
        responses:
        200:
            description: A user.
            examples:
            {"username": "tom"}
        """
        garment_id = request.path_params['garment_id']
        return JSONResponse(f"Got a garment with id: {garment_id}")

    async def update(self, request):
        """
        responses:
        200:
            description: A user.
            examples:
            {"username": "tom"}
        """
        return PlainTextResponse("A garment was updated")


    async def delete(self, request):
        """
        responses:
        200:
            description: A user.
            examples:
            {"username": "tom"}
        """
        return PlainTextResponse("A garment got deleted")
