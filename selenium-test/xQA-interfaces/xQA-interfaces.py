# coding=utf-8
import json
import requests
import datetime
import market_interfaces


postUrl = 'http://191.168.6.6:8180/xalms/engine/calc.action'

payloadHeader = {
    'Host': '191.168.6.6:8180',
    'Content-Type': 'application/json',
}
# 下载超时
timeOut = 250

if __name__ == '__main__':
    postUrl = postUrl
    header_data = payloadHeader
    instrumentList = [{'iCode':'000300','aType':'IDX_S','mType':'XSHG'}]
    begDate = '2019-06-01'
    endDate = '2019-06-30'
    sampleLenth = '0'

    interface = market_interfaces.calcTidxForReal(postUrl,header_data,instrumentList,begDate,endDate,sampleLenth)
    res = interface.result().text
    result = json.loads(res)
    print(result['result'])
