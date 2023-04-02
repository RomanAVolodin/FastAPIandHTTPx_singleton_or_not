import httpx
import uvicorn
from fastapi import FastAPI, Depends

from core import web
from core.web import get_httpx, get_httpx_singleton

app = FastAPI()


@app.on_event('startup')
async def startup_event():
    web.httpx_client = httpx.AsyncClient()


@app.on_event('shutdown')
async def shutdown_event():
    await web.httpx_client.aclose()


@app.get('/')
async def single(client: httpx.AsyncClient = Depends(get_httpx_singleton)):
    res = await client.get('https://yandex.ru')
    result = res.text
    return {
        'client_id': id(client),
        'result': result,
        'status': res.status_code
    }


@app.get('/sing')
async def single2():
    res = await web.httpx_client.get('https://yandex.ru')
    result = res.text
    return {
        'client_id': id(web.httpx_client),
        'result': result,
        'status': res.status_code
    }


@app.get('/mul')
async def multiple(client: httpx.AsyncClient = Depends(get_httpx)):
    res = await client.get('https://yandex.ru')
    result = res.text
    return {
        'client_id': id(client),
        'result': result,
        'status': res.status_code
    }


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        reload=True,
    )
