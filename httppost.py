import socket
import argparse, re
from urllib.parse import urlparse

parser = argparse.ArgumentParser()
parser.add_argument("--url", dest="target_host", help="url_target")
parser.add_argument("--username", dest="username", help="user")
parser.add_argument("--password", dest="password", help="password")
parser.usage = parser.format_help()
args = parser.parse_args()

host = args.target_host
user = args.username
passwd = args.password

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((urlparse(f'{host}').netloc,80))

header = """POST /wp-login.php HTTP/1.1\r
Host: blogtest.vnprogramming.com\r
Content-Type: application/x-www-form-urlencoded\r
Content-Length: {content_length}\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r
Connection: keep-alive\r
\r\n"""

body = "log={}&pwd={}\n\n".format(user,passwd)
header_bytes = header.format(content_length=len(body))
request = (header_bytes + body).encode()
s.send(request)
response = s.recv(4096)
s.close()
tmp = response.decode().count("Set-Cookie")
if "Set-Cookie" in response.decode() and "Location" in response.decode():
    print("User test đăng nhập thành công ")
else:
    print("User test đăng nhập thất bại")
