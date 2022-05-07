import pprint
import multiprocessing as mp
from pyfairdesk import WebSocketManager


if __name__ == "__main__":
    import pprint
    q = mp.Queue()
    proc = mp.Process(
        target=WebSocketManager,
        args=(q, ["btcusdt@markPrice"]),
        daemon=True
    )
    proc.start()

    while True:
        rdata = q.get()
        pprint.pprint(rdata)
