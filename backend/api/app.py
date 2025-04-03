from litestar import Litestar, get

from api.log import LogPlugin


@get("/")
async def index() -> str:
    return "Hello, world!"


app = Litestar(
    [
        index,
    ],
    plugins=[LogPlugin],
    debug=True,
)
