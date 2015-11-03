#!/usr/bin/python
import sys
import socket
#creating socket object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host name is localhost
host = 'localhost'
#check if any extra arguments are being passed
if len(sys.argv)> 1:
    #if port number is passed through the command line make that the port number
    port = int(sys.argv[1])
else:
    #if no command line argument passed than taking default port value
    port = 6789
#binding the host and port number together
serverSocket.bind((host,port))
#listen to the binded address
serverSocket.listen(5)
print 'please send your http request to '+str(host)+':'+ str(port)

while True:
    
    print 'Ready to serve...'
    #accepting connection from the client
    (client_connection, (client_ipaddress,client_port)) = serverSocket.accept()
    
    #server information
    serversocket_family = str(socket.AF_INET)
    serversocket_type = str(socket.SOCK_STREAM)
    serversocket_timeout = str(serverSocket.gettimeout())
    serversocket_hostname = str(socket.gethostname())
        
    #taking client request
    request = client_connection.recv(1024)
    #printing client request
    print request
    #printing client ip address and port number
    print "\n CLIENT IP ADDRESS: "+str(client_ipaddress)+"\n CLIENT PORT NUMBER: "+str(client_port)
    #processing the request for sending back requested file
    request_method = request.split(' ')[0]
    #checking the request method is GET
    if request_method == 'GET':
        #contains the name of the file required
        file_requested = request.split()
        file_requested = file_requested[1]
        
        if file_requested == '/HelloWorld.html':
            response_message = "HTTP/1.1 200 OK Content-Type: text/html \r\n\r\n"
            exact_name = file_requested[1:]
            file_handler = open(exact_name,'r')
            response = file_handler.read().replace('\n','')
            client_connection.send(response_message)
            client_connection.send(response.encode('utf-8'))
            #sending server information
            client_connection.send('\n SERVER INFORMATION')
            client_connection.send('\n HOSTNAME: '+ serversocket_hostname)
            client_connection.send('\n FAMILY: '+ serversocket_family)
            client_connection.send('\n TYPE: '+ serversocket_type)
            client_connection.send('\n TIMEOUT: '+ serversocket_timeout)
            client_connection.close()
        else:
            response_message = "HTTP/1.1 404 Not Found \r\n\r\n"
            response = '<html><body><p>Error 404: File not found</p><p>Python HTTP server</p></body></html>'
            client_connection.send(response_message)
            client_connection.send(response.encode('utf-8'))
            client_connection.close()
serverSocket.close()
#closing the server socket ideally it will never close