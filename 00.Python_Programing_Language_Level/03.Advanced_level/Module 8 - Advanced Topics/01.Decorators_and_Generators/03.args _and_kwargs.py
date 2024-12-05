"If when we create function we dont know hpw many parameters there will be then we can use *args and **kwargs "
# when we call function in the case of * args all the sent positional arguments will come back as tuple
def addition(*args):
    print(args)
    total = 0
    for item in args:
        total += int(item)
    return total
if __name__ == "__main__":
    value = addition(1,10,100)
    print(value)
# if we want to use named argument we use  **kwargs
def foo(**kwargs):
    print(kwargs)  # it will give us a dictionary

foo(a=1,b=1,c=100,d=[1,2,3])

# if we want to use both together
def foo(*args,**kwargs):
    print(args)
    print(kwargs)

foo(1,2,3,a=1,b=2,c=3)

# we can use any name after * and ** but the stars are important
