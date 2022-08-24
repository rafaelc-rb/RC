import socket
import threading
import time

# Variables that keeps the ip, port and format to encode message that will be sended
# ADDR variable receives the ip and port to guard the address information
SERVER = input('What\'s server IP:')
PORT = 5050
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

# Variable receives instance of the socket using AF_INET (ipv4) 
# and SOCK_STREAM (TCP Protocol). And then uses the uses the address
# to conect to the server.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

rsrcs = []

def handle_response():
    while True:
        fullresponse = client.recv(1024).decode()
        rsrcs = fullresponse.split(";")

        print("\n\n=============================")       
        print(f"""
          {rsrcs[0]} Info
        """)
        print("=============================")       
        for i in range(1, len(rsrcs)):
            print("  " + rsrcs[i]) 
        print("=============================")       


def send(requestion):
    client.send(requestion.encode(FORMAT))


def resource_request():
    while True:
        time.sleep(1.5)     
        print('''
        For a server resource checking choose:

        1.RAM Memory
        2.CPU
        3.Disk
        0.Exit
        ''')
        chosen_resource_option = int(input('What\'s ur choice? '))
        
        if(chosen_resource_option > 0 and chosen_resource_option < 4):
            send(str(chosen_resource_option))

        elif(chosen_resource_option == 0):
            exit()
            break

        else:
            err()

def err():
    print('''
    ===================
      Invalid Option!
    ===================
    ''')
    time.sleep(1)

def exit():
    print('''
    ====================
         Bye Bye✌️   
      See u next time!
    ====================
    ''')
    time.sleep(1)

def start():
    print('''
    =========================================
      Welcome to Server Resources Monitorer
    =========================================
    ''')
    thread1 = threading.Thread(target=handle_response)
    thread2 = threading.Thread(target=resource_request)
    thread1.start()
    thread2.start()

start()