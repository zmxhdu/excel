# coding = utf-8
import json
import pandas as pd
import numpy as np
import requests
import datetime
from market_interfaces.market_interfaces_tidx import CalcTidxForReal, CalcTidxInvlForReal, CalcTidx
from market_interfaces.market_interfaces_bond import CalcBond


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
    # instrumentList = [{'iCode': '000300', 'aType': 'IDX_S', 'mType': 'XSHG'},
    #                   {'iCode': '000016', 'aType': 'IDX_S', 'mType': 'XSHG'}]
    begDate = '2019-06-01'
    endDate = '2019-06-30'
    valueDate = '2019-06-30'
    sampleLenth = '0'

    # 指数批量
    # interface_tidxforreal = CalcTidxForReal(
    #     postUrl, header_data, instrumentList, begDate, endDate, sampleLenth)
    # 指数其他
    # interface_tidx = CalcTidx(postUrl, header_data, instrumentList, valueDate)
    # interfaces_data, res = interface_tidx.result()
    # res = interface_tidx.result().text

    instrumentList = [{'iCode': '151096', 'aType': 'SPT_BD', 'mType': 'XSHG'},
                      {'iCode': '151098', 'aType': 'SPT_BD', 'mType': 'XSHG'}]
    interface_bond = CalcBond(postUrl, header_data, instrumentList, valueDate)
    interfaces_data, res = interface_bond.result()
    resultList = json.loads(res.text)
    # print(result['result'])
    instrument_df = []
    result_df = []
    result_detail = []
    indexList_df = []
    if resultList['code'] == '-1':
        print(resultList['message'])
    else:
        for instrument, result in zip(instrumentList, resultList['result']):
            count = 0
            for instrument_key, instrument_value in instrument.items():
                if type(instrument_value) is list:
                    for i in range(0, len(instrument_value)):
                        if indexList_df is None:
                            index = instrument_key + '_' + str(i)
                            if count == 0:
                                indexList_df.append(index)
                            result_detail.append(instrument_value[i])
                else:
                    # print(instrument_key, instrument_value)
                    indexList_df.append(instrument_key)
                    result_detail.append(instrument_value)
                # if instrument_df is None:

            for result_key, result_value in result.items():
                if type(result_value) is list:
                    for i in range(0, len(result_value)):
                        index = result_key + '_' + str(i)
                        # print(index, result_value[i])
                        if count == 0:
                            indexList_df.append(index)
                        result_detail.append(result_value[i])
                else:
                    # print(result_key, result_value)
                    indexList_df.append(result_key)
                    result_detail.append(result_value)
            count += 1
        result_df.append(result_detail)
        print(indexList_df)
        print(result_df)

            # instrument_df_detail = pd.DataFrame(instrument, index=[0])
            # result_df_detail = pd.DataFrame(result_detail)
            # print(result_df_detail)

            # result_df_detail.to_excel('test.xlsx')
