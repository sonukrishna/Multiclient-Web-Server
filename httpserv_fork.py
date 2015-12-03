import socket
import os

host = '127.0.0.1'
port = 8007

def req_resp(sock_obj):
    request = sock_obj.recv(1024)
    print request
    response = """\
HTTP/1.1 200 OK

Hello,world!
"""
    sock_obj.send(response)

def main():
    host = '127.0.0.1'
    port = 8007
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print "connecting to the http port %s..."%port
    connection_list = []
    while 1:
        sock_obj, addr = server_socket.accept()
        connection_list.append(sock_obj)
        pid = os.fork()
        if pid == 0:  #child
            server_socket.close()
            req_resp(sock_obj)
            sock_obj.close()
            break
        else:
            print len(connection_list)
            sock_obj.close()

main()
