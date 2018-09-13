import socket

def handle_request(client):
    buf = client.recv(1024)
    a = "HTTP/1.1 200 OK\r\n\r\n"
    a = bytes(a, encoding = "utf8")
    client.send(a)
    client.send(bytes("Hello, World", encoding="utf8"))

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(5)


    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()

if __name__ == "__main__":
    main()