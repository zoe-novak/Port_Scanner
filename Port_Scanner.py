#                        __                                                     
#  ______   ____________/  |_    ______ ____ _____    ____   ____   ___________ 
#  \____ \ /  _ \_  __ \   __\  /  ___// ___\\__  \  /    \ /    \_/ __ \_  __ \
#  |  |_> >  <_> )  | \/|  |    \___ \\  \___ / __ \|   |  \   |  \  ___/|  | \/
#  |   __/ \____/|__|   |__|   /____  >\___  >____  /___|  /___|  /\___  >__|   
#  |__|   

# settings:

target_ip = "142.250.186.46" # <--- type your target ip you want to scan for open ports

max_port_scanned = 65535 # <--- type the the number of ports you want to scan


# the port scanner will print out open ports while scanning
# at the end it will return also a list of all open ports



# have fun



# ----------------code begin----------------

import socket
import threading
from queue import Queue

port_queue = Queue()
port_open = []
thread_list = []

def PortScan(port=8080):
    try:        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_ip, port))
        print("port {} open".format(port))
        return True
    except:
        return False

def PortScan_QueueFill(FromPort=0, ToPort=max_port_scanned):
    for port in range(FromPort, ToPort):
        port_queue.put(port)

def Worker_PortScan():
    while not port_queue.empty():
        port = port_queue.get()
        if PortScan(port):
            port_open.append(port)

PortScan_QueueFill()

thread_list = []

for thr in range(1000):
    thread = threading.Thread(target=Worker_PortScan)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print(port_open)