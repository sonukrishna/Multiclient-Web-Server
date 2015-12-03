import socket

host = '127.0.0.1'
port = 8006

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print "connecting to the http port %s..."%port

while 1:
    sock_obj, addr = server_socket.accept()
    request = sock_obj.recv(1024)
    print request

    response = """\ 
HTTP/1.1 200 OK

Hello,world!
"""
    sock_obj.send(response)
    sock_obj.close()
