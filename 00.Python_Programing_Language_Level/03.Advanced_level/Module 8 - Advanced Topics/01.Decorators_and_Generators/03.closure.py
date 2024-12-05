def addition (n1):

    def add(n2):
        return n1 + n2
    return add # it is returning  the function only not calling 

if __name__ == "__main__":
    ten_plus = addition(10)  # it returns a function
    hundred_plus = addition(100) # it returns a function

    print(ten_plus(5)) # add function takes a parameter so we have to send one parameter then it will add 5 with 10
    print(hundred_plus(20)) # same for this

# we can create more function
one_plus = addition(1)
print(one_plus(1))
print(one_plus(2))
print(one_plus(3))
 
# here we are creating function object one_plus,ten_plus,hundres_plus they are called closure
# To check if a function object is closure or not it is understandable by seeing the __closure__ property
# if it is not None then it is a closure
def addition (n1):

    def add(n2):
        return n1 + n2
    return add # it is returning  the function only not calling 
if __name__ == "__main__":
    one_plus = addition(1)
    print(one_plus(10))
    print(one_plus.__closure__)  # it is a closure
    print(addition.__closure__)  # addition function is not closure

"If the inside function does not access the data of outside function then there will be no closure"

def  addition (n1):

    def add(n2):
        return 1 + n2
    return add # it is returning  the function only not calling 
if __name__ == "__main__":
    one_plus = addition(1)
    print(one_plus(10))
    print(one_plus.__closure__)  # it is a closure
 