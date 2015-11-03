#!/usr/bin/python
#importing the socket library
import socket
#importing the sys inbuilt class to read arguments
import sys
#importing the timeit inbuilt class to measure RTT
import timeit

#creating an client object
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#checking if the argument length is greater than 1
if len(sys.argv)>1:
    host = sys.argv[1]
    port = int(sys.argv[2])
    file_required = sys.argv[3]
else:
    #if the length is not command line argument are not passed than taking some default values
    host = 'localhost'
    port = 6789
    file_required = '/HelloWorld.html'

#acquiring the hostname
clientsocket_hostname = str(socket.gethostname())
# getting the socket type
clientsocket_type =  str(socket.SOCK_STREAM)
# getting the socket family
clientsocket_family = str(socket.AF_INET)
# getting the timeout value
clientsocket_timeout = str(clientSocket.gettimeout())


print"\n"               
#connecting to the server
clientSocket.connect((host, port))
clientsocket_peername = str(clientSocket.getpeername())
#sending the request for the file
clientSocket.send("GET "+file_required+" HTTP/1.0\n\n")
#sending the client information to the server
clientSocket.send("\n CLIENT INFORMATION")
clientSocket.send("\n CLIENT HOSTNAME: "+clientsocket_hostname)
clientSocket.send("\n CLIENT FAMILY: "+clientsocket_family)
clientSocket.send("\n CLIENT TYPE: "+clientsocket_type)
clientSocket.send("\n CLIENT TIMEOUT: "+clientsocket_timeout)
clientSocket.send("\n CLIENT PEER NAME: "+clientsocket_peername)
#starting the timer to calculate the RTT
start_time = timeit.default_timer()
while True:
        #getting the file from the server
        response = clientSocket.recv(2048)
        #stopping the timer to get final reading of the RTT
        elapsed = timeit.default_timer() - start_time
        if response == "": break
        #printing the file received
        print response,
#printing the RTT value
print "\n RTT: "+str(elapsed)
#closing the client socket
clientSocket.close()
print "\ndone"
#printing the DONE to show end of program