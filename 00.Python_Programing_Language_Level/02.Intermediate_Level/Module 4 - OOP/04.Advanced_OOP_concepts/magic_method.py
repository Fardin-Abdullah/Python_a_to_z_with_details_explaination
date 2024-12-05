"Magic method are called those method which have double underscore also they are called dunder method "
"because of using double underscore"

x = "Bangladesh"
print(x.__len__())
x = [1,2,3]
print(x.__len__())
x = {"a":"A","b":"B"}
print(x.__len__()) 
# in python in class of str,list,dictionary,set there is __len__() method implemented

x = 100
print(str(x))
print(x.__str__())
# here x is an int we can send x in a str() function because in int class there is __str__() method 
# implemented
print(dir(int))

# we can do different types of work with same operator for example + , because what will do this operator 
# it is told in __add__ method
x = 100
y = 10
print(x.__add__(y))
a = "Bangla"
b = "desh"
print(a.__add__(b))