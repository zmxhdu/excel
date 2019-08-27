# coding=utf-8
import json
import requests
import datetime
import market_interfaces


# 批量接口
postUrl = 'http://191.168.6.6:8180/xalms/engine/calcBatch.action'

payloadHeader = {
    'Host': '191.168.6.6:8180',
    'Content-Type': 'application/json',
}
# 下载超时
timeOut = 250


if __name__ == '__main__':
    header_data = payloadHeader
    instrumentList = [{'iCode': '000300', 'aType': 'IDX_S', 'mType': 'XSHG'},
                      {'iCode': '000016', 'aType': 'IDX_S', 'mType': 'XSHG'}]
    begDate = '2019-06-01'
    endDate = '2019-06-30'
    valueDate = '2019-06-30'
    sampleLenth = '0'

    # 指数批量
    interface_tidxforreal = market_interfaces.CalcTidxForReal(
        postUrl, header_data, instrumentList, begDate, endDate, sampleLenth)
    # 指数其他
    interface_tidx = market_interfaces.CalcTidx(postUrl, header_data, instrumentList, valueDate)
    res = interface_tidx.result().text
    result = json.loads(res)

    if result['code'] == '-1':
        print(result['message'])
    else:
        for result_detail in result['result']:
            print(result_detail)
