
#-*- coding: utf-8 -*-

import urllib.request
import re

pythontagurl = "http://www.cnblogs.com/itech/category/170012.html"
pythonarticleurlregrex = "(<a.*?href=\"http://www.cnblogs.com/itech/archive.*?>([Pp]ython.*?)</a>)"

# get the page content string which contains all python article links
pythontagpage = urllib.request.urlopen(pythontagurl)
pythontagstr = ""
for line in pythontagpage.readlines():
   try:
     newline = line.decode('utf-8', 'strict')
     #print(newline)
   except:
     continue
   pythontagstr +=  newline
pythontagpage.close()

# get all link and sort 
pythonlinkandtiles = re.findall(pythonarticleurlregrex, pythontagstr)
d = dict()
for link, title in pythonlinkandtiles:
  d[title] = link
pythontitles = list(d.keys())
pythontitles.sort()
pythonarticles = []
for py in pythontitles:
  pythonarticles.append(d[py])

# generate pythonindex.html
pythonindex = open("pythonindex.html", "w",encoding='utf-8')
pythonindex.write("<html>")
pythonindex.write("<head>")
pythonindex.write("<meta http-equiv='Content-Type' content='text/html; charset=utf-8'/>")
pythonindex.write("<title>Python - iTech's Blog</title>")
pythonindex.write("</head>")
pythonindex.write("<body>")
pythonindex.write("Total number is :" + str(len(pythonarticles)) + "</br>")
for pa in pythonarticles:
  pythonindex.write(pa)
  pythonindex.write("</br>")
pythonindex.write("</body>")
pythonindex.write("</html>")
pythonindex.close()
