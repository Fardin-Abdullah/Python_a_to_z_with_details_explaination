"In python there is built in function for sorting for making built in function in  python timsort algorithm is used"
li = [1,2,3,4,5,6,2,3]
li.sort()
print(li)
li.sort(reverse=True)
print(li)

countries = ["Bangladesh","Japan","Australia","Canada","Singapore"]
countries.sort()
print(countries)

li = [1,3,4,5,6,2,3]
nums = sorted(li)
print(nums)
print(li)

# sorted() can be used on other iterables also
tpl = (3,8,1,4,6,2)
result = sorted(tpl)
print(result)

fruits = [("orange",3),("apple",2),("guava",8)]
# first element of tuple do protinidhitto for tuple
print(sorted(fruits))

def compare_function(item):
    return item[1]

fruits = [("orange",3),("apple",2),("guava",8)]
print(sorted(fruits,key = compare_function))
print(sorted(fruits,key = compare_function,reverse=True))

from operator import itemgetter
fruits = [("orange",3),("apple",2),("guava",8)]
print(sorted(fruits,key=itemgetter(1)))
print(sorted(fruits,key=itemgetter(0)))
print(sorted(fruits,key=itemgetter(1,0)))
