import socket
import argparse, re
from urllib.parse import urlparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("--url", dest="target_host", help="url target argument")
args = parser.parse_args()

host = args.target_host
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((urlparse(f'{host}').netloc,80))
s.send(b"GET / HTTP/1.1\r\nHost:blogtest.vnprogramming.com\r\n\r\n")
response = s.recv(4096).decode()
s.close()
filter_res = re.search(r">.*&", response).group()
print(filter_res[1:-1:])
