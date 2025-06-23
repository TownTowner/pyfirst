import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connect to server, IP_ADDRESSconnect(("IP_ADDRESS    s.connect(("127.0.0.1", 50007))  # connect to server, 127.0.0.1 -> localhost, 50007 -> port number of server
    s.connect(("127.0.0.1", 50007))
    while True:  # send data to server, 1024 -> buffer size, bytes
        data = input("Enter message: ")
        # s.sendall(data.encode())
        # send data to server, encode() -> convert string to bytes, decode() -> convert bytes to string
        s.sendall(data.encode())
        data = s.recv(1024)  # receive data from server, 1024 -> buffer size, bytes
        print(f"Received {data.decode()}")
