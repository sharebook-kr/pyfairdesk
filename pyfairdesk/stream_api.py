"""
Fairdesk Websocket API
"""
import asyncio
import json
import multiprocessing as mp
import websockets


class WebSocketManager:
    """Websocket manager class
    """
    def __init__(self, dqueue: mp.Queue, stream: list):
        self.queue = dqueue
        self.stream = stream
        self.run()

    async def ws_client(self):
        """client
        """
        uri = "wss://www.fairdesk.com/ws"
        async for websocket in websockets.connect(uri, ping_interval=None):
            try:
                subscribe_req = {
                    "method": "SUBSCRIBE",
                    "params": self.stream,
                    "id": 1
                }
                await websocket.send(json.dumps(subscribe_req))

                while True:
                    data = await websocket.recv()
                    data = json.loads(data)
                    self.queue.put(data)
            except websockets.ConnectionClosed:
                # https://websockets.readthedocs.io/en/stable/reference/client.html
                self.queue.put("ConnectionClosedError")
                continue

    def run(self):
        """_summary_
        """
        asyncio.run(self.ws_client())


if __name__ == "__main__":
    import pprint
    q = mp.Queue()
    proc = mp.Process(
        target=WebSocketManager,
        #args=(q, ["btcusdt@depth10", "ethusdt@depth10"]),
        #args=(q, ["btcusdt@kline_1m"]),
        #args=(q, ["btcusdt@markPrice"]),
        #args=(q, ["btcusdt@ticker"]),
        args=(q, ["btcusdt@trade"]),
        daemon=True
    )
    proc.start()

    while True:
        rdata = q.get()
        pprint.pprint(rdata)
