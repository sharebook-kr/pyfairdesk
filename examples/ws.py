import websockets
import asyncio
import json
import pprint

async def ws_client():
    uri = "wss://www.fairdesk.com/ws"

    async with websockets.connect(uri, ping_interval=None) as websocket:
        fmt = {
            "method": "SUBSCRIBE",
            "params": [ "btcusdt@trade" ],
            "id": 1
        }
        data = json.dumps(fmt)
        await websocket.send(data)

        while True:
            data = await websocket.recv()
            data = json.loads(data)
            pprint.pprint(data)

async def main():
    await ws_client()

asyncio.run(main())

