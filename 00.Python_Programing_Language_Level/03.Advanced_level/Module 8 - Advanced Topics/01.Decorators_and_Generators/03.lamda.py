# We can create small small function using lambda function it is called annonymous function cause we don't 
# have to give this name lambda expression returns a function object we can use many parameteres in this function
# but the expression has to be one 


one_plus = lambda x: x + 1
print(one_plus(3))
print(type(one_plus))
add = lambda x,y : x + y
print(add(3,4))

# in nested function the second function access the data of outside function like this lambda can access the variable outside of it's scope
def addition(n1):
    return lambda n2 : n1 + n2

if __name__ == "__main__":
    one_plus = addition(1)
    print(one_plus(10))

