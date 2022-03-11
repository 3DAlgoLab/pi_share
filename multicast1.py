import socket
import struct


message = b'very important data'
multicast_group = ('224.3.29.71', 10000)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(0.2)
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)


try:
    # send data to the multicast group
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, multicast_group)
    # Look for response from all recipients
    while True:
        print('waiting to receive')
        try:
            data, server = sock.recvfrom(100)
        except socket.timeout:
            print('no more responses')
        else:
            print('received {!r} from {}'.format(data, server))

finally:
    print('closing socket')
    sock.close()
