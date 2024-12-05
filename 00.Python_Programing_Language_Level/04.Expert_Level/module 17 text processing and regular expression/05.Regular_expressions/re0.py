# when this concept is in hand you will think you are a big programmar

# suppose in a string there are multiple countries name we have to find which country has land at last

s = "Afganistan,America,Bangladesh,Canada,Denmark,England,Greenland,Iceland,Netherlands,New Zealand,Sweden,Switzerland"
print(s)

countries = s.split(",") # turned string into list
print(countries)

li = [item for item in countries if item.endswith("land")] # checking if there is land at last list comprehension 
print(li)

li = [item for item in countries if item.endswith ("land") or item.endswith("lands")]
print(li)

import re

s = "Afganistan,America,Bangladesh,Canada,Denmark,England,Greenland,Iceland,Netherlands,New Zealand,Sweden,Switzerland"
li = re.findall(r'(\w+lands*)',s)
print(li)

# if we want to use regular expression then we have to import re module
match = re.search("Bangla","Bangladesh") # in this search function first srgument is what we are finding and this function return an object
print(match) # and second argument is where we are finding

# first argument is called regular expression
print(match.group()) # if we call group() method of that object we get the string if we dont find our string the search function returns None

match = re.search("desh","Bangladesh")
print(match.group())

match = re.search('des','Bangladesh')
print(match.group())

match = re.search('dets','Bangladesh')
#print(match.group())
print(match)
print(type(match))
print(match is None)