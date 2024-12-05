class A:
    def hello(self):
        print("Hello from class A")

class B(A):
    pass

class C(A):
     def hello(self):
        print("Hello from class A")

    

class D(B,C):
    pass

obj =D()
obj.hello()