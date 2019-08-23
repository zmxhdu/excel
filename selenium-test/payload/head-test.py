# conding = utf-8


import requests
import time
import datetime
import json
import urllib3

url = 'http://191.168.0.61:8080/xqa/engine/calc.action'
response = urllib3.connection_from_url(url)
print(response.host)