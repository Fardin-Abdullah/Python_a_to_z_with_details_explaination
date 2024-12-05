# suppose we want to make a server about car at start we will implement get and post method 
# if we want to create any car we will use post method
# if we want to get detail informations of car we use get method

from http.server import HTTPServer, SimpleHTTPRequestHandler
from dataclasses import dataclass
from urllib.parse import urlparse,parse_qs
import json

@dataclass
class Car:
    car_id:str
    name: str
    manufacturer: str
    year : int
    price : int

car_db = dict()
HOST,PORT = "localhost",8888

class SimpleServer(SimpleHTTPRequestHandler):

    def _send_400(self):
        self.send_response(400)
        self.send_header("Content-type","text/html")
        self.end_headers()
    
    def _send_200(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
    
    def do_GET(self):
        parsed_url = urlparse(self.path)
        qs = parse_qs(parsed_url.query)
        if 'id' not in qs or len(qs['id']) == 0:
            self.__send__400()
            html_content = "<html><body>id missing</body></html"
            self.wfile.write(html_content.encode())
            return
        car_id = qs['id'][0]
        car = car_db[car_id]

        self._send_200()
        details = "Car Name: {}<br>Manufacturer: {}<br>Year: {}"
        details += "<br>Price: {}<br>"
        details = details.fprmat(car.name,car.manufacturer,car.year,car.price)
        html_content = "<html><body>{}</body></html>".format(details)
        self.wfile.write(html_content.encode())
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            c = json.loads(post,data)
            print(c)
            car = Car(c['id'],c['name'],c['manufacturer'],c['year'],c['price'])
            car_db[car.car_id] = car
        except KeyError:
            self.__send__400()
            html_content = "<html><body><h1>Missing required field(s)"
            html_content += "<h1></body></html>"
            self.wwfile.write(html_content.encode())
            return 
        self._send_200()

if __name__ == "__main__":
    car = Car("1","Camry","Toyota",2022,40000)
    car_db[car.car_id] = car

    simple_server = HTTPServer((HOST,PORT),SimpleServer)
    print("Starting server ...\n")
    try:
        simple_server.serve_forever()
    except KeyboardINterrupt:
        pass
    simple_server.server_close()
    print("Server shutting down ...")

# int his cose do post method
# for posting we send data in server and to read data we use self.rfile.read() method