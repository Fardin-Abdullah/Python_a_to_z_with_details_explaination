#Iterator is an special type of object.The characteristic of it is it knows the current state of it for this
# it can tell the next step of it and can find it we have to call next to find the next step

#Suppose we want to create an iterator from a string for this we have to call iter function

city = "Dhaka"
city_itr = iter(city) # in iter function we are sending string argument for this city_itr is an instance of
# str_iterator class
print(city_itr)
print(type(city_itr))

print(next(city_itr))
print(next(city_itr))
print(next(city_itr))
print(next(city_itr))
print(next(city_itr))
#print(next(city_itr) when we call next function in next function which object is sent in, next function it will call the next function of that class
# here we are sending object of str_iterator class for this next function will call the __next__() method of this class in next method of 
# this class it is said how to get the next element and when there is no element throw stop iteration

city = "Dhaka"
for c in city: # here an iterator is creating from city string by python and everytime is calling next() function . when next() function 
    #gives stopitearation it exits from the loop but it doesn't give any erro to user why ?
    print(c)

# creating an iterator
class my_range:  # it works like range(n)
    def __init__(self,n): # we are telling here index will start from 0 and highest value will be n - 1
        self.index = 0
        self.max_index = n - 1
    
    def __iter__(self): # here it only returns self for this method python can undesrtand that this class is an iterator
        return self
    def __next__(self):  
        if self.index <= self.max_index:
            self.index += 1
            return self.index - 1
        else:
            raise StopIteration()

if __name__ == "__main__":
    for i in my_range(5):
        print(i)
# if we don't use for loop here
if __name__ == "__main__":
    it = my_range(5)
    while True:
        try:
            print(next(it)) # we can also use here it.__next__()
        except StopIteration:
            break

"Which object can make iterator (if we use iter() function retuns an iterator ) they are called iterable"
"In python list,tuple,set,dictionary all are iterable"

li = [1,2,3]
it = iter(li)
print(type(it),it)

tpl = (1,2,3)
it = iter(tpl)
print(type(it),it)

st = {1,2,3}
it = iter(st)
print(type(it),it)

dt = {"a":"A","b":"B","c":"C"}
it = iter(dt)
print(type(it),it)

# There is a module itertools it can help to work with iterator easily 