import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("blogtest.vnprogramming.com",80))
s.send(b"GET / HTTP/1.1\r\nHost:blogtest.vnprogramming.com\r\n\r\n")
r = s.makefile()
print("Title of Wordpress is: \n")
for line in r.readlines():
    if '<title>' in line:
        print(line[8:18])
        s.close()
