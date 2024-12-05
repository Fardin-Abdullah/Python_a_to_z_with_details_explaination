import re

s = "Abcd 1234 - 33"
result = re.sub(r'\d','0',s)
print(result)

s = "22/07/2017,10/01/2017,01/01/2018"
new_s = re.sub(r'(\d{3})/(\d{2})/(\d{4})',r'\3-\2-\1',s)
print(new_s)

new_s = re.sub(r'(\d{2})/(\d{2})/(\d{4})','\g<3>-\g<2>-\g<1>',s)
print(new_s)
