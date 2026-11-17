import asyncio
import gzip
import aiohttp
from aiohttp import web
from aiohttp.test_utils import TestClient, TestServer

async def verify_aiohttp():
    async def echo(request):
        return web.Response(body=await request.read())

    async def form(request):
        return web.json_response(dict(await request.post()))

    async def websocket(request):
        ws = web.WebSocketResponse(max_msg_size=64)
        await ws.prepare(request)
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                await ws.send_str(msg.data)
        return ws

    app = web.Application()
    app.add_routes([web.post('/echo', echo), web.post('/form', form), web.get('/ws', websocket)])
    async with TestClient(TestServer(app)) as client:
        async with client.post('/echo', data=gzip.compress(b'compressed payload'), headers={'Content-Encoding': 'gzip'}) as response:
            assert response.status == 200
            assert await response.read() == b'compressed payload'
        async with client.post('/form', data={'query': 'ACTG'}) as response:
            assert await response.json() == {'query': 'ACTG'}
        async with client.ws_connect('/ws', compress=15) as ws:
            await ws.send_str('echo')
            assert (await ws.receive(timeout=5)).data == 'echo'
            await ws.send_str('x' * 128)
            message = await ws.receive(timeout=5)
            assert message.type == aiohttp.WSMsgType.CLOSE, message
            assert message.data == 1009, message
    print(f'PASS aiohttp {aiohttp.__version__}: gzip HTTP, forms, compressed WebSocket, message-size rejection')


if __name__ == '__main__':
    asyncio.run(verify_aiohttp())

