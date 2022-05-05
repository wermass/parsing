from urllib.request import urlopen
import collections
import re


html = urlopen("file:///home/dmitry/test/stepik/2.html").read().decode('utf-8')
s = str(html)
regex = '<code>(.*?)</code>'
ans = 
l = re.findall(regex, s)

print(collections.Counter(l).most_common())
