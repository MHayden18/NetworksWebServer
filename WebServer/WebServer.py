# Import socket module
from socket import *    

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
#Fill in start
serverPort = 8018
#serverAddress = "127.0.0.1"
serverAddress = "192.168.0.15"
serverSocket.bind((serverAddress, serverPort))
serverSocket.listen(1)
#Fill in end

# Server should be up and running and listening to the incoming connections
while True:
    print ('Ready to serve...')
    
    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()   #Fill in end
    
    # If an exception occurs during the execution of try clause
    # the rest of the clause is skipped
    # If the exception type matches the word after except
    # the except clause is executed
    try:
        # Receives the request message from the client
        message = connectionSocket.recv(1024).decode()    #Fill in end
        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]
        # Because the extracted path of the HTTP request includes
        # a character '/', we read the path from the second character
        f = open(filename[1:])

        # Store the entire content of the requested file in a temporary buffer
        outFile = f.read()  #Fill in start  #Fill in end
        # Send the HTTP response header line to the connection socket
        #Fill in start
        #outHeader = "HTTP/1.1 200 OK\r\n"
        #for i in range(0, len(outHeader)):
        #    connectionSocket.send(outHeader[i].encode())
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        #Fill in end
        
        # Send the content of the requested file to the connection socket
        for i in range(0, len(outFile)):
            connectionSocket.send(outFile[i].encode())
        connectionSocket.send("\r\n".encode())
        
        # Close the client connection socket
        connectionSocket.close()

    except IOError:
        # Send HTTP response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found \r\n\r\n".encode())
        f = open("404Error.html")
        #f = open("404_NotFound.html")  #Fill in start    #Fill in end
        outFile = f.read()

        for i in range(0, len(outFile)):
            connectionSocket.send(outFile[i].encode())
        connectionSocket.send("\r\n".encode())
        # Close the client connection socket
        connectionSocket.close()

serverSocket.close()  
