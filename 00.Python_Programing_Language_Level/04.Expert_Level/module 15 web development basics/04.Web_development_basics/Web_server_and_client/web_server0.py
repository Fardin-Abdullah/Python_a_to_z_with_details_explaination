# we will learn how to make web server by using http.server module and also will use requests modules with this we will create web client
# http.server module---> web server
# requests module---> web client

from http.server import HTTPServer,SimpleHTTPRequestHandler

HOST,PORT = "localhost",8888
class SimpleServer(SimpleHTTPRequestHandler): # it is a class which inherit a class
    pass

if __name__ == "__main__":
    simple_server = HTTPServer((HOST,PORT),SimpleServer)
# in previous line we created a server here which port and host have to use we have said it in first argument
# and in second class we said in which class there will be request handling
    simple_server.serve_forever()
    simple_server.server_close()

# now if we open not search http://localhost:8888 (in search bar) we will find the directory of this program 
# now we will implement do_GET() method in SimpleServer class