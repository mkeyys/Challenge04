import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("blogtest.vnprogramming.com",80))

header = """POST /wp-login.php HTTP/1.1\r
Host: blogtest.vnprogramming.com\r
Content-Type: application/x-www-form-urlencoded\r
Content-Length: {content_length}\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r
Connection: keep-alive\r
\r\n"""
user= input("user:")
passwd = input("pass:")
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
