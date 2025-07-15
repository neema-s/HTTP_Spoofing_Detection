import socket
import ssl

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server_socket.bind(('0.0.0.0', 443))  # server is listening on all interfaces
server_socket.listen(1)

print("Waiting for connection...")
client_socket, addr = server_socket.accept()

secure_socket = context.wrap_socket(client_socket, server_side=True)
print(f"SSL connection established with {addr}")

data = secure_socket.recv(1024).decode()
print(f"Received domain: {data}")

spoofed_domain = input("Enter spoofed domain: ")
secure_socket.send(spoofed_domain.encode())

secure_socket.close()





