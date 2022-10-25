#!/usr/bin/env python3
import socket
import re
import argparse
from urllib.parse import urlparse

parser = argparse.ArgumentParser()
parser.add_argument("--url", dest='target_host', help="Host target")
parser.add_argument("--download", dest='download', help="file path to download")
args = parser.parse_args()

host = args.target_host
download_file = args.download

def recv_all(the_socket):
    total_data=[]
    data = the_socket.recv(8192)
    while (len(data) > 0):
        total_data.append(data)
        data = the_socket.recv(8192)
    data = b''.join(total_data)
    return data

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
domain_name = urlparse(f'{host}').netloc
s.connect((domain_name,80))
header =  ( f'GET {download_file} HTTP/1.1\r\n'
            f'Host: {domain_name}\r\n'
            f'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36\r\n'
            f'Accept: */*\r\n'
            f'Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5\r\n'
            f'Accept-Encoding: gzip, deflate\r\n\r\n'
).encode()

s.send(header)

response = recv_all(s)
if b"HTTP/1.1 200 OK" in response:
    length_file = re.findall(b"Content-Length: ([0-9]+)\r\n", response)[0].decode()
    print("Kích thước file ảnh: " + length_file + " bytes")

    response_body = b''
    response_header = response.split(b'\r\n\r\n')[0]
    image_content = response[len(response_header)+4:]
    file_name = download_file.split("/")[-1]
    f = open(f"./file_upload/{file_name}", "wb")
    f.write(image_content)
    f.close()
else:
    print("Không tồn tại file ảnh.")
    exit()
