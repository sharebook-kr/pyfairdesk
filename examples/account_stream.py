import pprint
import multiprocessing as mp
import pyfairdesk
from pyfairdesk import WebSocketManager

if __name__ == "__main__":
    with open("../fairdesk.key", "r", encoding="utf-8") as f:
        lines = f.readlines()
        key = lines[0].strip()
        secret = lines[1].strip()

    exchange = pyfairdesk.Fairdesk(key, secret)
    ws_token = exchange.create_websocket_token()
    ws_token = ws_token['data']['wsToken']

    q = mp.Queue()
    proc = mp.Process(
        target= WebSocketManager,
        args=(q, [ws_token]),
        daemon=True
    )
    proc.start()

    while True:
        rdata = q.get()
        pprint.pprint(rdata)

