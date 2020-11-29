import socket, struct


def int32_to_ip(int32):
    test = socket.inet_ntoa(struct.pack('!L', int32))
    return test

