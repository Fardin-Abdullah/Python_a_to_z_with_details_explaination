from http.server import HTTPServer,SimpleHTTPRequestHandler
HOST,PORT = "localhost",8888
class SimpleServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

        print("Command: ")
        print(self.command)
        print("Path: ")
        print(self.path)
        print("Request headers:")
        print(self.headers)

        html_content = "<html><body><h1>Hello Boss!</h1></body></html>"
        self.wfile.write(html_content.encode())


simple_server = HTTPServer((HOST,PORT),SimpleServer)
print("Starting Server...\n")
try:
    simple_server.serve_forever()
except KeyboardInterrupt:
    pass
simple_server.server_close()
print("Server shutting down ...")


# now install curl and open a new terminal and command curl http://localhost:8888
# now install curl and open a new terminal and command curl http://localhost:8888/car
# now we will get some output in this terminal client send get command and as path sent /car there are also some commands except get


