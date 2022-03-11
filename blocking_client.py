import socket

sock = socket.socket()
# host = socket.gethostname()
host = '192.168.0.104'
sock.connect((host, 12345))

sock.setblocking(0)

# Or simply omit this line as by default TCP sockets
# are in blocking mode

data = b"Hello Python\n" * 10 * 1024 * 1024  # Huge amount of data to be sent
assert sock.send(data)			        # Send data till true
