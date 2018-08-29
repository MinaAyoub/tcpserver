import socket

print ("ready to accept...")

host = '127.0.0.1'
port= 23

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))
s.listen(5)
client, clientaddr = s.accept()
print(str(clientaddr) + "connected")

while True:
    data = client.recv(1024).decode('utf-8')
    if not data:
        break
    data = data.upper()
    print ("Sending: " + data)
    client.send(data.encode('utf-8'))

    # client.close()

