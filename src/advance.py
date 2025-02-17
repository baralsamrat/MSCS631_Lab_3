#!/usr/bin/env python3
import os
import ssl
import base64
from socket import *
from dotenv import load_dotenv
# SENDER_EMAIL=
# EMAIL_PASSWORD=
# RECIPIENT_EMAIL=

# Load environment variables from .env file
load_dotenv()

def main():
    # Load sensitive data from environment variables
    sender_email = os.getenv("SENDER_EMAIL")
    email_password = os.getenv("EMAIL_PASSWORD")  # May be empty if not required
    recipient_email = os.getenv("RECIPIENT_EMAIL")
    
    # Check if required variables are provided
    if not sender_email or not recipient_email:
        print("Error: SENDER_EMAIL and RECIPIENT_EMAIL must be set in the environment.")
        return

    mailserver = 'smtp.gmail.com'
    port = 587

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    print("Server response after connection:", recv)

    heloCommand = 'EHLO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv = clientSocket.recv(1024).decode()
    print("Server response after EHLO:", recv)

    starttls = "STARTTLS\r\n"
    clientSocket.send(starttls.encode())
    recv = clientSocket.recv(1024).decode()
    print("Server response after STARTTLS:", recv)

    context = ssl.create_default_context()
    clientSocket = context.wrap_socket(clientSocket, server_hostname=mailserver)

    clientSocket.send(heloCommand.encode())
    recv = clientSocket.recv(1024).decode()
    print("Server response after EHLO (post TLS):", recv)

    # If an email password is provided, perform AUTH LOGIN; otherwise, skip authentication.
    if email_password:
        authLogin = "AUTH LOGIN\r\n"
        clientSocket.send(authLogin.encode())
        recv = clientSocket.recv(1024).decode()
        print("Server response after AUTH LOGIN:", recv)

        username_encoded = base64.b64encode(sender_email.encode()).decode() + "\r\n"
        clientSocket.send(username_encoded.encode())
        recv = clientSocket.recv(1024).decode()
        print("Server response after sending username:", recv)

        password_encoded = base64.b64encode(email_password.encode()).decode() + "\r\n"
        clientSocket.send(password_encoded.encode())
        recv = clientSocket.recv(1024).decode()
        print("Server response after sending password:", recv)
        if not recv.startswith('235'):
            print("235 reply not received, authentication failed.")
            clientSocket.close()
            return
    else:
        print("No password provided, skipping authentication.")

    mailFrom = f"MAIL FROM:<{sender_email}>\r\n"
    clientSocket.send(mailFrom.encode())
    recv = clientSocket.recv(1024).decode()
    print("Server response after MAIL FROM:", recv)
    if not recv.startswith('250'):
        print("250 reply not received from server.")
        clientSocket.close()
        return

    rcptTo = f"RCPT TO:<{recipient_email}>\r\n"
    clientSocket.send(rcptTo.encode())
    recv = clientSocket.recv(1024).decode()
    print("Server response after RCPT TO:", recv)
    if not recv.startswith('250'):
        print("250 reply not received from server.")
        clientSocket.close()
        return

    dataCommand = "DATA\r\n"
    clientSocket.send(dataCommand.encode())
    recv = clientSocket.recv(1024).decode()
    print("Server response after DATA command:", recv)
    if not recv.startswith('354'):
        print("354 reply not received from server.")
        clientSocket.close()
        return

    message = ("Subject: Test Email\r\n"
               "\r\n"
               "This is a test email sent from my Python SMTP client using environment variables.\r\n")
    clientSocket.send(message.encode())

    endmsg = "\r\n.\r\n"
    clientSocket.send(endmsg.encode())
    recv = clientSocket.recv(1024).decode()
    print("Server response after sending message data:", recv)

    quitCommand = "QUIT\r\n"
    clientSocket.send(quitCommand.encode())
    recv = clientSocket.recv(1024).decode()
    print("Server response after QUIT command:", recv)

    clientSocket.close()

if __name__ == "__main__":
    main()
