
import socket

s = socket.socket()

host = socket.gethostname()
port = 12345

print(host, port)

s.bind((host, port))
s.listen(5)

while True:
    conn, addr = s.accept()		# accept the connection

    data = conn.recv(1024)
    while data:			        # till data is coming
        print(data.decode('utf-8'))
        data = conn.recv(1024)
    print("All Data Received")  # Will execute when all data is received
    conn.close()
    break
