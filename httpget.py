import socket
import re
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("blogtest.vnprogramming.com",80))
s.send(b"GET / HTTP/1.1\r\nHost:blogtest.vnprogramming.com\r\n\r\n")
response = s.recv(4096).decode()
s.close()
filter_res = re.search(r">.*&", response).group()
print(filter_res[1:-1:])
