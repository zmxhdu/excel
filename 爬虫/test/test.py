# coding = utf-8
import urllib.request

response = urllib.request.urlopen('http://191.168.2.37:8888/secure/Dashboard.jspa')
print(response.read().decode('utf-8'))
