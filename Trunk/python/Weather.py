


def ToGB(str):
  return str.decode('utf-8')

def TestUrlOpen():
  import urllib.request
  page = urllib.request.urlopen("http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName=58367")
  lines = page.readlines()
  page.close()
  document = ""
  for line in lines :
    document = document + line.decode('utf-8')

  from xml.dom.minidom import parseString
  dom =parseString(document)
  strings = dom.getElementsByTagName("string")
  print (strings[6].childNodes[0].data + " " + strings[7].childNodes[0].data)

  

def TestSuds() :
  from suds import WebFault
  from suds.client import Client 
  url = 'http://webservice.webxml.com.cn/WebServices/WeatherWS.asmx?WSDL'
  client = Client(url)
  print (client)
  print (client.service.getWeather('58367'))


#TestUrlOpen()
TestSuds()



