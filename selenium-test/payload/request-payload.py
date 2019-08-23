# coding = utf-8

import json
import requests
import datetime

postUrl = 'http://191.168.6.6:8180/xalms/engine/calc.action'
# payloadData数据
payloadData = {
    "begDate": "2019-01-01",
    "endDate": "2019-03-31",
    "isNeedInst": "false",
    "list": [{"begDate":"2018-12-31","portCode":"PGA","endDate":"2019-03-31"},
             {"begDate":"2018-12-31","portCode":"PTI","endDate":"2019-03-31"},
             {"begDate":"2018-12-31","portCode":"000004","endDate":"2019-03-31"},
             {"begDate":"2018-12-31","portCode":"000003","endDate":"2019-03-31"},
             {"begDate":"2018-12-31","portCode":"BX0010","endDate":"2019-03-31"},
             {"begDate":"2018-12-31","portCode":"BX0012","endDate":"2019-03-31"},
             {"begDate":"2018-12-31","portCode":"BX0011","endDate":"2019-03-31"},
             {"begDate":"2018-12-31","portCode":"PTI_CAPITAL","endDate":"2019-03-31"},
             {"begDate":"2018-12-31","portCode":"PSD","endDate":"2019-03-31"},
             {"begDate":"2018-12-31","portCode":"BX0015","endDate":"2019-03-31"}],
    "method": "calcAcctHoldSegment",
    "nodeList":"[1771,1772,1773,1774,1775]",
    "portCode": "BX0010"
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
