"Function it'self is an object"
def add(a,b):
    return a+b

fn = add
result = fn(2,3)
print(result)
print(add)
print(type(add)) # it will show that it is an instance of class function
print(dir(add)) # the attributes of this object 
print(add.__name__) # an attribute of the add object 
print(fn.__name__) # same as previous line so python function is also an object

"Function inside function ( nested function )"

def fnc1():
    print("I am fnc 1")

    def fnc2():
        print("I am fnc 2")
    fnc2()

fnc1()

"Nonlocal"

def addition(n1,n2): # n1,n2 are parameter of this function
    def add(): # it can read the variables of outside function  but can not change it
        result = n1 + n2
        print("Inside add() function, result :",result)
    add()

if __name__ == "__main__":
    n1,n2 = 10,5
    addition(n1,n2)

# changing the code

def addition(n1,n2): # n1,n2 are parameter of this function
    result = 0
    def add(): # it can read the variables of outside function  but can not change it but we can change it
        # if we want in next function we will do it
        result = n1 + n2
        print("Inside add() function, result :",result)
    add()
    print("Result:",result)

if __name__ == "__main__":
    n1,n2 = 10,5
    addition(n1,n2)


def addition(n1,n2): # n1,n2 are parameter of this function
    result = 0
    def add(): # it can read the variables of outside function  but can not change it but we can change it
        nonlocal result # it's basically bring the nonlocal result variable inside the function
        result = n1 + n2
        print("Inside add() function, result :",result)
    add()
    print("Result:",result)

if __name__ == "__main__":
    n1,n2 = 10,5
    addition(n1,n2)

"Return of Function"
# function can return function
def addition(n1,n2):

    def add():
        return n1 + n2
    return add # be careful add and add() has differences return add will not execute the function it will 
    # return function object on the other hand return add() will execute the function and will return the value of the function
if __name__ == "__main__":
    fnc = addition(10,20)
    print(fnc)
    print(type(fnc))
    print(fnc())

"Closure"



