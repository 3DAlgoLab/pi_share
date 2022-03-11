import socket
from multiprocessing.pool import ThreadPool
import time

_pool = ThreadPool(4)
_sock = socket.socket()


def just_proc(id, duration):
    for i in range(10):
        print(f"ID {id}: {i}")
        time.sleep(duration)


def send_proc(sock):
    # host = socket.gethostname()
    try:
        host = '192.168.0.104'
        sock.connect((host, 12345))

        sock.setblocking(1)

        # Or simply omit this line as by default TCP sockets
        # are in blocking mode

        data = b"Hello Python\n" * 10 * 1024 * 1024  # Huge amount of data to be sent
        sock.send(data)			        # Send data till true
    except Exception as e:
        print("E:", e)
        print("")


if __name__ == "__main__":
    _pool.apply_async(send_proc, (_sock,))
    # _pool.apply_async(just_proc, ('A', 0.5))
    # _pool.apply_async(just_proc, ('B', 0.6))
    input("Waiting...")
    _sock.close()
    input("Sock close result?")
    _pool.terminate()
