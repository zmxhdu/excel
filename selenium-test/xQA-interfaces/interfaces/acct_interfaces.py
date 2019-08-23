# coding = utf-8

import json
import requests
import datetime

postUrl = 'http://191.168.6.6:8180/xalms/engine/calc.action'
# payloadData数据
payloadData = {
    "focusNum": "1",
    "gCode": "GR_190810142716fc20f0",
    "isNeedInst": "false",
    "list": ["000003",
             "000004",
             "BX0010",
             "BX0011",
             "BX0012",
             "BX0015"],
    "method": "calcAcctClassifyRatioJ",
    "nodeList": ["1890"],
    "priceType": "3",
    "tDate": "2019-03-31"
}


# 请求头设置
payloadHeader = {
    'Host': '191.168.6.6:8180',
    'Content-Type': 'application/json',
}
# 下载超时
timeOut = 250

r = requests.post(postUrl, data=json.dumps(payloadData), headers=payloadHeader)
dumpJsonData = json.dumps(payloadData)
print(f"dumpJsonData = {dumpJsonData}")
res = requests.post(postUrl, data=dumpJsonData, headers=payloadHeader, timeout=timeOut, allow_redirects=True)
# 下面这种直接填充json参数的方式也OK
# res = requests.post(postUrl, json=payloadData, headers=header)
print(f"responseTime = {datetime.datetime.now()}, statusCode = {res.status_code}, res text = {res.text}")
