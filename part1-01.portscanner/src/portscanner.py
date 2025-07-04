#!/usr/bin/env python3
import sys
import socket

def get_accessible_ports(address, min_port, max_port):
    found_ports = []

    for i in range(min_port, max_port + 1):
        try:

            s = socket.socket()
            s.connect((address, i))
            found_ports.append(i)

        except:
            print("Not a valid port: ")

        s.close()

    return found_ports

def main(argv):
    address = sys.argv[1]
    min_port = int(sys.argv[2])
    max_port = int(sys.argv[3])
    ports = get_accessible_ports(address, min_port, max_port)
    for p in ports:
        print(p)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("usage: python %s address min_port max_port" % sys.argv[0])
    else:
        main(sys.argv)
