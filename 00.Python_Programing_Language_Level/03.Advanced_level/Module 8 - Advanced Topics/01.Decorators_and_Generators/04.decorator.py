def deco(fnc): # this function takes a function as parameter this function returns wrapper function
    def wrapper(): # in this function it calls that function which has come as parameter and also print before and after
        print("Before")
        fnc()  # in this function it calls that function which has come as parameter
        print("After")
    return wrapper

def hello(): # it prints hello on screen
    print("Hello")

fnc = deco(hello) # here we are calling deco function and sending hello function as an argument and deco returns a function
print(fnc)
fnc() # here we called the function fnc() it will execute the wrapper function

# here deco function is a decorator
# if we send any function in this decorator first it will print before and then will do the work of that function we have sent and then it will print after
# to do this work there is a beautiful system in python
def deco(fnc):
    def wrapper():
        print("Before")
        fnc()
        print("After")
    return wrapper

@deco
def hello():
    print("Hello")
hello()

# this will give us the same output as before
# if we want to use decorator with any function we write @ before that function then write the decorator name
# in this case in hello function there is not any parameter if there is a parameter then how we should create decorator function?let's see
def deco(fnc):
    def wrapper(*args,**kwargs):
        print("Before")
        fnc(*args,**kwargs)
        print("After") 
    return wrapper

@deco
def hello ():
    print("Hello")

@deco
def hello_name(name):
    print("Hello",name)

@deco
def add(n1,n2):
    print(n1+n2)

hello()
print()
hello_name("World")
print()
print()
add(3,5)

# here we used *args and **kwargs so we can use parameters as many as we want, we use same decorator in 3 functions
# first decorator doesn't take any parameter
# second one takes one parameter
# third one takes two parameter
# one function takes how much time to run we need to find it. we used timeit module. now we will use decorator to do the same thing

import time

def timer(fnc):
    def wrapper(*args,**kwargs):
        start = time.time()
        fnc(*args,**kwargs)
        end = time.time()
        print("Function took{:.2f} seconds".format(end-start))
    return wrapper

@timer
def sleep_fnc(s):
    time.sleep(s)

@timer
def sleep_double(s):
    time.sleep(2*s)

sleep_fnc(3)
sleep_double(2)