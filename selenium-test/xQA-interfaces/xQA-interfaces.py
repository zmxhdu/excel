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
    result = json.loads(res.text)
    # print(result['result'])

    result_df = pd.DataFrame()

    if result['code'] == '-1':
        print(result['message'])
    else:
        for result_detail, instrument in zip(result['result'], instrumentList):
            # for instrument_key, instrument_value in instrument.items():
            #     if type(instrument_value) is list:
            #         for i in range(0, len(instrument_value)):
            #             index = instrument_key + '_' + str(i)
            #             print(index, instrument_value[i])
            #     else:
            #         print(instrument_key, instrument_value)
            # for result_key, result_value in result_detail.items():
            #     if type(result_value) is list:
            #         for i in range(0, len(result_value)):
            #             index = result_key + '_' + str(i)
            #             print(index, result_value[i])
            #     else:
            #         print(result_key, result_value)
            instrument_df_detail = pd.DataFrame(instrument, index=[0])
            result_df_detail = pd.DataFrame(result_detail)
            # print(result_df_detail)
            # result_df_detail = pd.merge(instrument_df_detail, result_df_detail)

            # result_df.merge(result_df,result_df_detail)
            result_df_detail.to_excel('test.xlsx')
