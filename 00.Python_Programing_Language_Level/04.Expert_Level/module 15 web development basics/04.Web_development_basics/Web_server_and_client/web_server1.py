from http.server import HTTPServer,SimpleHTTPRequestHandler
HOST,PORT = "localhost",8888
class SimpleServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

        html_content = "<html><body><h1>Hello World!</h1></body></html>"
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
