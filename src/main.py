import os
from socket import *
from dotenv import load_dotenv
# MAIL_SERVER=smtp.gmail.com
load_dotenv()

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Get the mail server from the environment; if empty, default to smtp.gmail.com.
mailserver = os.getenv("MAIL_SERVER")
if not mailserver:
    mailserver = "smtp.gmail.com"

print("Using mail server:", mailserver)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))

recv = clientSocket.recv(1024).decode()
print("Server response after connection:", recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print("Server response after HELO:", recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
