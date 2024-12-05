import re
s = "Bangladesh"
match = re.search('.',s) # this dot means alphabate
print(match.group())

match = re.search('B.n', s) # a
print(match.group())

match = re.search('B.n...',s) # bangla
print(match.group())

s = "Bangladesh is our homeland"
match = re.search('............',s)
print(match.group()) # here the dot is also counting the space

s = "Bangladesh is our homeland"
match = re.search("o\w\w",s) # after o taking two alphabates
print(match.group())

match = re.search("i\w\w",s)
#print(match.group())
print(match)

match = re.search("B\w+h",s) # it will fix the previous problem
print(match.group())

# what if 
match = re.search('B.+h',s)
print(match.group())  # regular expression is greedy 

# if we want it will stop at first h what will we do 

match = re.search('B.+?h',s)
print(match.group())

