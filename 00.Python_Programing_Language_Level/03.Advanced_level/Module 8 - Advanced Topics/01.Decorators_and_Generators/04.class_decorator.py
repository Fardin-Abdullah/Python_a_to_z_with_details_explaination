class A:
    def __init__(self):
        pass

obj = A()
#obj() # it will give error

# it will give us error and it is impossible
# so __call__ method wil make it possible

class A :
    def __init__(self):
        pass
    def __call__(self):
        print("Now I am callable")

obj = A()
obj()

# no using this idea we can make a class decorator

class DecoratorClass:
    def __init__(self,fnc):
        self.fnc = fnc
    def __call__(self,*args,**kwargs):
        print("Before")
        self.fnc(*args,**kwargs)
        print("After")
@DecoratorClass
def hello():
    print("Hello")

@DecoratorClass
def hello_name(name):
    print("Hello",name)

hello()
print()
hello_name("Python")