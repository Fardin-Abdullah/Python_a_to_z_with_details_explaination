"Those which ca contain data are called container for example list,tuple,set,dictionary etc"
print("1---->")
li = [1,2,3]
print("1.",5 in li)
print("2.",2 in li)
print("2.---->")
tpl = (1,2,3,4)
print("1.",4 in tpl)
print("2.",5 in tpl)
print("3---->")
st = {2,4,5,7}
print("1.",9 in st)
print("2.",5 in st)
print("4---->")
dt = {1:"one",2:"two",3:"three"}
print("1.",1 in dt)
print("2.",4 in dt)
print("3.","one" in dt)
print("4.","one" in dt.values())
print("5.","four" in dt.values())
print("6.",1 in dt.keys())
print("7.",4 in dt.keys())

"We can  run loop on container easily for example watch this"
li = [1,2,3,4,5]
for item in li :
    print(item)