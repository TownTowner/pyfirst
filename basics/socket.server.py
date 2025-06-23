import socket

# socket.AF_INET -> ipv4, socket.AF_INET6 -> ipv6
# socket.SOCK_STREAM -> TCP, socket.SOCK_DGRAM -> UDP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 50007))
    s.listen()
    # conn -> socket, addr -> ip address and port number of client
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            # receive data from client, 1024 -> buffer size, bytes
            data = conn.recv(1024)
            if not data:  # if no data, break
                break
            conn.sendall(data)  # send data to client
