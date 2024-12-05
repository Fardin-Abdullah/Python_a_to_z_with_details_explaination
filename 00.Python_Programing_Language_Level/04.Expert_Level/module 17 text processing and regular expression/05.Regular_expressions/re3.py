# suppose there is a file named file.text in this file there are 3 lines
# one: Bangladesh is our Country
# two: Bangla is our language
# three:Python is a programming language
# now we want to read this file in a program and will put it in a string and will do regular expression and try to sepearate every line
# first know that ^ caret symbol is start in re and dollar sign is end let's see example
import re
s = "Bangla,english,bangla"
print(re.findall(r'english',s))

print(re.findall(r'^english',s))

print(re.findall(r'english$',s))

print(re.findall(r'^Bangla',s))

print(re.findall(r'bangla$',s))

s = "Bangla,english,Bangla"

print(re.findall(r'bangla$',s))

print(re.findall(r'bangla$',s,re.IGNORECASE))

print(re.findall(r'bangla$',s,re.I))


