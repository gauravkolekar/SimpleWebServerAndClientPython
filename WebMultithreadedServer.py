#!/usr/bin/python
"""
Citation: http://seanmcgary.com/posts/threaded-tcp-server-in-python
"""
#importing the in build socket class
import socket
#importing the in build thread class
import thread
#importing the in build sys class to read command line arguments
import sys

#checking the length of the command line argument
if len(sys.argv)> 1:
    port = int(sys.argv[1])
else:
    #if no command line argument passed than taking default port value
    port = 6789

# creating a function to handle
def connection_handler(clientsocket, clientaddr):
    print "Accepted connection from: ", clientaddr
    
    while True:
        request = clientsocket.recv(1024)
        #printing client requesr
        print request
        #splitting the request for processing
        file_requested = request.split()
        #getting the name of the file to be given back
        file_requested = file_requested[1]
        
        if file_requested == '/HelloWorld.html':
            response_message = "HTTP/1.1 200 OK Content-Type: text/html \r\n\r\n"
            exact_name = file_requested[1:]
            file_handler = open(exact_name,'r')
            response = file_handler.read().replace('\n','')
            
            clientsocket.send(response_message)
            #sending the file
            clientsocket.send(response.encode('utf-8'))
            #sending the server information
            clientsocket.send('\n SERVER INFORMATION')
            clientsocket.send('\n HOSTNAME: '+ serversocket_hostname)
            clientsocket.send('\n FAMILY: '+ serversocket_family)
            clientsocket.send('\n TYPE: '+ serversocket_type)
            clientsocket.send('\n TIMEOUT: '+ serversocket_timeout)
                        
            clientsocket.close()
            #closing client socket after sending the information
        else:
            response_message = "HTTP/1.1 404 Not Found \r\n\r\n"
            response = '<html><body><p>Error 404: File not found</p><p>Python HTTP server</p></body></html>'
            clientsocket.send(response_message)
            clientsocket.send(response.encode('utf-8'))
            clientsocket.close()

if __name__ == "__main__":

    host = 'localhost'
        
    addr = (host, port)

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket_family = str(socket.AF_INET)
    serversocket_type = str(socket.SOCK_STREAM)
    serversocket_timeout = str(serversocket.gettimeout())
    serversocket_hostname = str(socket.gethostname())
    
        
    serversocket.bind(addr)

    serversocket.listen(5)

    while True:
        print "Ready to serve..."
        print "Server is listening for connections on "+str(host)+ " "+str(port)+"\n"

        clientsocket, clientaddr = serversocket.accept()
        thread.start_new_thread(connection_handler, (clientsocket, clientaddr))
    serversocket.close()
