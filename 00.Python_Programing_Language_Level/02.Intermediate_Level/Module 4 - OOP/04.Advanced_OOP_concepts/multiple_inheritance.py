"In python one class can inherit many classes it is called multiple iheritance"
class A:
    def fnc(self):
        print("Hello from A")
class B:
    def fnc(self):
        print("Hello from B")
class C(A,B):
    pass

obj = C()
obj.fnc() # Hello from A

class D(B,A):
    pass

obj = D()
obj.fnc() # Hello from B

# so we can see that if we inherit multiple classes it works according to order it is called method resolution order or mro
print(D.mro())
print(C.mro())