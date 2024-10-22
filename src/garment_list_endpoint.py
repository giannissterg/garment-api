from starlette.responses import PlainTextResponse
from starlette.endpoints import HTTPEndpoint

class GarmentListEndpoint(HTTPEndpoint):
    async def get(self, request):
        """
        responses:
        200:
            description: A list of users.
            examples:
            [{"username": "tom"}, {"username": "lucy"}]
        """
        return PlainTextResponse("A list of garments")


    async def post(self, request):
        """
        responses:
        200:
            description: A user.
            examples:
            {"username": "tom"}
        """
        return PlainTextResponse("Garment created")

