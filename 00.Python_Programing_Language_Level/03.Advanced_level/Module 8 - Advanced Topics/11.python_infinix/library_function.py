li = [1,2,3,4,5,6,7,3,6,1,0]
a,b,c = sum(li),max(li),min(li)
print(a,b,c)
print(reversed(li))
# complexity of these functions are O(n)
s = "Python"
print(reversed(s))
print("".join(reversed(s)))
print(pow(2,4))

print(abs(-1))

print(divmod(10,3))

n = 10
a = -10

print(bin(n))
print(bin(a))

print(oct(n))
print(oct(a))

print(hex(n))
print(hex(a))

import math
print(math.pi)
print(round(math.pi,2))
print(round(math.pi,3))
print(round(math.pi,4))

# for ASCII use ord()

for item in ['a','e','i','o','u','0','9']:
    print(ord(item))

for item in [97,98,66,48,66,65,57]:
    print(chr(item))

# suppose we have to many conditions all have to be true we use all function for this and if all have to false we use any()

cond1,cond2,cond3,cond4,cond5,cond6 = 1==1,2>1,3<4,1==1,2<1,3>4
print(all([cond1,cond2,cond3]))
print(all([cond1,cond2,cond3,cond4]))
print(all([cond4,cond5]))
print(any([cond1,cond2,cond3,cond4,cond5]))

prog_lang = ["C","C+","Python","Java","Go"]
i = 1
li = []
for item in prog_lang :
    li.append((i,item))
    i += 1
print(li)

# to do this easily we use enumerate

print(enumerate(prog_lang,start=1)) # it returns an iterable object

print([x for x in enumerate(prog_lang,start=1)])
# we converting it into list
print(list(enumerate(prog_lang,start=1)))

for item in zip([1,2,3],('one','two','three')):
    print(item)

li0 = ["a","b","c","d"]
li1 = [1,2,3,4,5]
li2 = [1,5,7,8,9,28]
list(zip(li0,li1,li2))

# when we want to use any function on every elements of any iterable we use map see example
print(list(map(int,['1','10','100'])))

sqr = map(lambda x: pow(x,2),[1,2,3])
print(list(sqr))

names = ["raafi","ilmaa","araf","raiyan","arabi"]
names = list(map(lambda x: x.title(),names))
print(names)

def add_100(x):
    return x + 100

print(list(map(add_100,[1,2,3])))

# suppose we want even numbers only
nums = list(range(1,21))
print(nums)
even_nums = filter(lambda x: x % 2 == 0, nums)
print(list(even_nums))

x = 1
print(eval('x+1'))
x = 10
print(eval('divmod(10,3)'))
print(eval('4 > 3 and 3 > 2'))
