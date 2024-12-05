class A:
    def hello(self):
        print("Hello from class A")

class B(A):
    def hello(self):
        print("Hello from class B")
    
class C(A):
    pass

class D(B,C):
    pass

obj =D()
obj.hello()