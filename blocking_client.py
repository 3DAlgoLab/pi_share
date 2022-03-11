import socket

sock = socket.socket()
# host = socket.gethostname()
host = 'tal-works'
sock.connect((host, 12345))

sock.setblocking(1)

# Or simply omit this line as by default TCP sockets
# are in blocking mode

data = "Hello Python\n" * 10 * 1024 * 1024  # Huge amount of data to be sent
assert sock.send(data)			        # Send data till true
