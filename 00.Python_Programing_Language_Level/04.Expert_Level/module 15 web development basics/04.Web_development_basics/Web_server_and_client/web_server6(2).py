import requests
import json

def create_car():
    car2 = {
        "id":"2",
        "name": "Corolla",
        "year": 2022,
        "price":32000
    }

    url = 'http://localhost:8888'
    for car in [car2]:
        response = requests.post(url, data=json.dumps(car),auth=('dimik','python'))

        print(response.status_code)
        print(response.content)
        if response.status_code == 200:
            print("new car created with id",car['id'])
        print()

def get_car(car_id):
    url = 'http://localhost:8888'
    params = {'id':car_id}
    response = requests.get(url,params)
    print(response.status_code)
    print(response.text)

def update_car_price(car_id,price):
    print("updating car",car_id)
    url = 'http://localhost:8888'
    car = {"id":car_id,"price":price}
    response = requests.patch(url, data=json.dump(car),auth=('dimik','python'))
    print(response.status_code)
    print(response.content)

def delete_car(car_id):
    print("deleting car",car_id)
    url = 'http://localhost:8888/delete/' + str(car_id)
    response = requests.delete(url,auth=('dimik','python'))
    print(response.status_code)
    print(response.text)


if __name__ == "__main__":
    print("creating cars")
    create_car()
    get_car("2")
    update_car_price("2",50000)
    get_car("2")
    delet_Car(2)
    get_car(2)