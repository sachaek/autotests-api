import asyncio

import websockets
from websockets import ServerConnection


async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение: {message}")
        response = f"Сервер получил: {message}"
        for i in range(5):
            await websocket.send(response)


async def main():
    server = await websockets.serve(echo, host="localhost", port=8756)
    print("Websocket сервер запущен на ws://localhost:8756")
    await server.wait_closed()

asyncio.run(main())
