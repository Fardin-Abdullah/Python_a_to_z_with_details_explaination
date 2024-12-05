import re
s = "<li>Fardin</li><Abdullah</li><li>Raafi</li><li>Ilmaa</li>"
result = re.findall(r'<li>(.*?)</li>',s)
print(result)