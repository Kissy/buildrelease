﻿
# -*- coding: UTF-8 -*-

def TestHttpGet():
    import httplib2

    #httplib2.debuglevel = 1

    word='china'
    urlstr = 'http://fy.webxml.com.cn/webservices/EnglishChinese.asmx/TranslatorString' + '?wordKey=' + word

    h = httplib2.Http('.cache') 
    response,content = h.request(urlstr)

    #for item in response.items(): print(item)
    print(content.decode('gb2312'))
    #print(content)
    
def TestHttpPost():
  import httplib2
  from urllib.parse import urlencode    
  
  #httplib2.debuglevel = 1

  word='us'
  urlstr = 'http://fy.webxml.com.cn/webservices/EnglishChinese.asmx/TranslatorString'

  data={'wordKey':word} 
  
  h = httplib2.Http('.cache')
  response,content = h.request(urlstr, 'POST', urlencode(data), headers={'Content-Type': 'application/x-www-form-urlencoded'})  

  #for item in response.items(): print(item)
  print(content.decode('utf-8'))
  #print(content)
  
TestHttpGet()
TestHttpPost()