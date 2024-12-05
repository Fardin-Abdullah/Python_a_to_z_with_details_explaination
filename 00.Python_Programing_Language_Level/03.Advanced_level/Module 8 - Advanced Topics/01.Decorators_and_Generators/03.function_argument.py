"We can send argument in two different ways"
def foo(a,b,c):
    print("Value of a",a)
    print("Value of b",b)
    print("Value of c",c)

#positional argument / non keyword argument  
fn = foo(1,2,3)  # a = 1, b = 2 , c = 3 this system of sending argument is called positional argument 
print(fn)
#named argument  / keyword argument

if __name__ == "__main__":
    print(foo(1,2,3))
    print(foo(b=2,c=3,a=1))
    print(foo(1,2,c=3))
    print(foo(1,b=2,c=3))

    #print(foo(a=1,2,3)) right---> print(foo(2,3,a=1))
    print(foo(b=2,c=3,a=1))

# always first positional argument then named argument