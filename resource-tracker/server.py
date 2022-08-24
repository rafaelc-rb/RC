import socket
import threading
import time
import monitor

# Set the server ip and port to variables, and then bind them to 
# another variable called "ADDR", and set the uft-8 format to a 
# variable that will be used to encode the message that will be 
# send to the client.
input('Press enter to start the server.')
SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'

# Socket instance, AF_INET by using ipv4 and SOCK_STREAM by using TCP protocol.
# And then assigns the IP address and the port number to a socket instance using bind(ADDR) method.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
print(f"[STARTED] Server started at: { ADDR } 🔥")

connections = []

# Method send_resources(connection), first feedback the user with a print in cosole
# then for every resource requested send the information encoded to the client
# who requested it, and then clean the vector that was keeping the information.
# @param receives the client connection info to send the data.
def send_resources(connection):
    print(f"[SENDING] Sending response to {connection['addr']}")
    send_resource = connection['resource']
    connection['conn'].send(send_resource.encode())
    time.sleep(0.3)

# Method handle_clients(conn, addr), responsible for handling with the clients connections 
# and decoding the message sended by the client and prepare the message to be sended
# back calling the monitor.py methods. And calls the send_resources() method to send
# the message.
# @param receives the message and address from the client.
def handle_clients(conn, addr):
    print(f"[NEW CONNECTION] A new user has connected by address: { addr } 🔥")
    global connections

    while(True):
        requestion = conn.recv(1024).decode(FORMAT)
        if(requestion):
            if(requestion == "1"):
                resource = monitor.mem()
            elif(requestion == "2"):
                resource = monitor.cpu()
            elif(requestion == "3"):
                resource = monitor.disk()
            
            connection_map = {
                "conn": conn,
                "addr": addr,
                "resource": resource
            }

            connections.append(connection_map)
            send_resources(connection_map)

# Method start() starts the socket and keeps it listening for new connections.
# Create a thread for every connection it calls the handle_clients() method.
def start():
    print("[STARTING] Starting Socket!")
    server.listen()
    while(True):
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clients, args=(conn, addr))
        thread.start()

start()