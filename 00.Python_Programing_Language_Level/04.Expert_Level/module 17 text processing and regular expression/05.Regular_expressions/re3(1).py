import re
with open("file.txt","r") as f:
    text = f.read()
print(text)

print(re.findall(r'^.*?$',text))
print(re.findall(r'^.*?$',text,re.MULTILINE)) # re.MULTILINE is a flag and it will give an empty string at last to avoid this
print(re.findall(r'^.+?$',text,re.MULTILINE))

