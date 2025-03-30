from litestar import Litestar, get
from litestar.plugins.structlog import StructlogPlugin


@get("/")
async def index() -> str:
    return "Hello, world!"


@get("/favicon.ico")
async def favicon() -> None:
    """
    Litestar doesn't default this, so we'll just make the exception go away for now.
    """
    return


app = Litestar(
    [index, favicon],
    plugins=[StructlogPlugin()],
    debug=True,
)
