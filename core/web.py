import httpx

httpx_client: httpx.AsyncClient | None


def get_httpx_singleton() -> httpx.AsyncClient:
    return httpx_client


async def get_httpx() -> httpx.AsyncClient:
    async with httpx.AsyncClient() as aclient:
        yield aclient
