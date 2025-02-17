# MSCS631_Lab_3
Samrat Baral

Lab 3

University of the Cumberlands

2025 Spring - Advanced Computer Networks (MSCS-631-M40) - Full Term
Dr. Yousef Nijim

February 15, 2025

SMTP programming In this lab, you will acquire a better understanding of SMTP protocol. You will also gain experience in implementing a standard protocol using Python. See the attached document for full lab instructions.

# Screenshot
![1](/Capture-1.PNG)

# Ouput 
```bash
python .\main.py
Using mail server: smtp.gmail.com
Server response after connection: 220 smtp.gmail.com ESMTP 006d021491bc7-5fcb16aae06sm2666970eaf.15 - gsmtp

Server response after HELO: 250 smtp.gmail.com at your service

```

# Experience and Challenges:

In completing this SMTP client assignment, I gained a deeper insight into the SMTP protocol,
particularly the necessity of securing connections with STARTTLS and authenticating using AUTH LOGIN.
Handling the base64 encoding of credentials and correctly formatting each command (with CRLF sequences)
were critical to successfully communicating with Gmail’s SMTP server.

One of the main challenges was adapting the simple socket-based client to work with a server that requires
secure connections and authentication. Learning to use Python's ssl module and properly manage the SMTP
authentication handshake provided invaluable hands-on experience in network security and protocol debugging.
