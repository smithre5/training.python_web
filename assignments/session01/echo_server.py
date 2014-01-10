import socket
import sys

"""
Initial Test sequence:
/c/7_PYTHON/2Q_UW/WEEK_FOLDERS/session01/gitcode_7JanCopy>python
Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import echo_server
>>> echo_server.server()
making a server on 127.0.0.1:10000
waiting for a connection
. . . (I invoked <CTRL-C> here) . . . 
/c/7_PYTHON/2Q_UW/WEEK_FOLDERS/session01/gitcode_7JanCopy>
"""

def server(log_buffer=sys.stderr):
    # set an address for our server
    address = ('127.0.0.1', 10000)
    MAX_SERVER_CONNECTIONS = 1
    # TODO: Replace the following line with your code which will instantiate 
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    # solution: This could have been "default", but wanted to be explicit.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # TODO: Set an option to allow the socket address to be reused immediately
    #       see the end of http://docs.python.org/2/library/socket.html
    # solution:  as a socket jockey from C/C++, I know about SO_REUSEADDR, 
    # and I know python socket is a thinly wrapped interface to C libraries, 
    # so I just googled 'python setsockopt SO_REUSEADDR'.
    # This must be executed before bind is called in order to work.
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # log that we are building a server
    print >>log_buffer, "making a server on {0}:{1}".format(*address)
    
    # TODO: bind your new sock 'sock' to the address above and begin to listen
    #       for incoming connections
    sock.bind(address)
    sock.listen(MAX_SERVER_CONNECTIONS)
   
    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print >>log_buffer, 'waiting for a connection'

            # TODO: make a new socket when a client connects, call it 'conn',
            #       at the same time you should be able to get the address of 
            #       the client so we can report it below.
            conn, client_addr = sock.accept()
            try:
                print >>log_buffer, 'connection - {0}:{1}'.format(*client_addr)

                # the inner loop will receive messages sent by the client in 
                # buffers.  When a complete message has been received, the 
                # loop will exit
                while True:
                    # TODO: receive 16 bytes of data from the client. Store
                    #       the data you receive as 'data'.  
                    data = conn.recv(16)
                    print >>log_buffer, 'received "{0}"'.format(data)
                    # TODO: you will need to check here to see if any data was
                    #       received.  If so, send the data you got back to 
                    #       the client.  If not, exit the inner loop and wait
                    #       for a new connection from a client
                    if not data:
                        break
                    conn.sendall('%s' % (data))
            finally:
                # TODO: When the inner loop exits, this 'finally' clause will
                #       be hit. Use that opportunity to close the socket you
                #       created above when a client connected.
                conn.close()
            
    except KeyboardInterrupt:
        # TODO: Use the python KeyboardInterrupt exception as a signal to 
        #       close the server socket and exit from the server function. 
        sock.close()


if __name__ == '__main__':
    server()
    sys.exit(0)