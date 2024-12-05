import re
# if we use any regular expresiion multiple times then we should compile it before otherwise it will take time to compile every time
# if we use 
#result = re.findall(pattern,string)
# we should write
#cpat = re.compile(pattern)
#result = cpat.findall(string)
 
# suppose we have different dayes in a text we have to find it
text = "This is line 1, Date is 2017/06/01.And there is another date: 2017-07-01.THe third and final date is 2017/08/30."
pat = re.compile(r'(\d{4})[-/](\d{2})[-/](\d{2})')
print(pat)

print(re.compile("(\\d{4})[-/](\\d{2})[-/](\\d{2})"))
print(type(pat))
result = pat.findall(text)
print(result)
print(dir(pat))

s = "Abcd 1234 - 33"
result = re.sub(r'\d','0',s)
print(result)
