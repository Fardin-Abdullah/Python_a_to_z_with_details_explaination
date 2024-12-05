# visit http://books.toscrape.com/index.html
# then all category name and url of them (travel,art....
# see html source of the page on webpage click right button 
# and find where are the names of categories and link of them

import requests
import re

url = "http://books.toscrape.com/index.html"
response = requests.get(url)
print(response.ok)
text = response.text
print(len(text))

# Extract the part containing categories
result = re.findall(r'<div class="side_categories">(.*?)</div>', text, re.M | re.DOTALL)
print(len(result))
print(type(result))
print(result)  # We got the part in between div

# Compile the pattern for category links (to find a certain category link)
category_pat = re.compile(r'<li>\s*<a href="(.*?)">\s*(.*?)\s*</a>', re.M | re.DOTALL)
result = re.findall(category_pat, text)
print(result[0])
print(len(result))

for item in result:
    print(item)


# now we want to find find every books link of a category 
# for example science fiction category if we click on this category find link for every books