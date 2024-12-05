# we will find out how get phone number from a string
import re
text = "Phone number: 01742091116."
match = re.search('\d+',text)
print(match.group())

text = "house number: 5, phone number: 01742091116. "
match = re.search('\d+',text)
print(match.group())

# now to get mobile number we have to update regular expression
text = "house number: 5, phone number: 01742091116. "
match = re.search('\d{11}',text)
print(match.group())

# what if 
text = "house number: 5, phone number: 017 42091116."
match = re.search('\d{11}',text)
#print(match)

# fixing previous problem
text = "house number: 5, phone number: 01742091116."
match = re.search('\d{3}\s*\d{8}',text) # whitespace is \s and \s* means it can occur 0 time or multiple time
print(match.group())

# and if there is + after \s that means minimum one time there will be \s

# if there are multiple phone numbers 
text = "multiple phone number,01742091116,01742091115,01742091114,00000000000 123-123"
result = re.findall(r'\d{3}\s*\d{8}',text)
print(result)

# but the last number is not a phone number how to fix it
# see the condition of bangladesh phone number first 01 and then is wlaways among these digit 5,6,7,8,9 and then 8 digits
text = "multiple phone number,01742091116,01742091115,01742091114,00000000000 123-123"
result = re.findall(r'01[56789]\s*\d{8}',text)
print(result)



