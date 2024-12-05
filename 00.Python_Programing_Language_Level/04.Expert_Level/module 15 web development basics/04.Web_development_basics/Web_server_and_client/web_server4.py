# now we will make a client
import requests
import json

def create_car():
    car2 = {
        "id":"2",
        "name":"Corolla",
        "manufacturer":"Toyota",
        "year":2022,
        "price":32000}
    
    car3 = {
        "id":"3",
        "name":"Camry",
        "manufacturer":"Toyota",
        "year":2022,
        "price":37000}
    
    car4 = {
        "id":"4",
        "name":"Prado",
        "manufacturer":"Toyota",
        "year":2022,
        "price":80000
        }
    
    url = 'http://localhost:8888'
    for car in [car2,car3,car4]:
        response = requests.post(url,data=json.dumps(car))
        print(response.status_code)
        if response.status_code == 200:
            print("new car created with id",car["id"])
        print()

def get_car(car_id):
    url = 'http://localhost:8888'
    params = {'id':car_id}
    response = requests.get(url,params)
    print(response.status_code)
    print(response.text)

if __name__ == "__main__":
    print("creating car")
    create_car()
    for i in range(1,5):
        create_car()
        for i in range(1,5):
            print("getting car data from server for car id",i)
            get_car(i)

#HTTP methods are get,post,head,put,patch,delete
# we call put method to change any resource also patch is used for changed but for a certain field