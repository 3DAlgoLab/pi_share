import socket
import struct


multicast_group = "224.3.29.71"
server_address = ('', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(server_address)

# tell the os to add the socket to the multicast group on all interfaces
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# loop
while True:
    print('\nWaiting to receive message')
    data, address = sock.recvfrom(1024)

    print("Received {} bytes from {}".format(len(data), address))
    print(data)
    print('sending ack. to', address)
