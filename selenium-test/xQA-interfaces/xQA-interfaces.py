# coding = utf-8
import json
from market_interfaces.market_interfaces_tidx import CalcTidxForReal, CalcTidxInvlForReal, CalcTidx
from market_interfaces.market_interfaces_bond import CalcBond
from market_interfaces_batch.market_interfaces_bond_batch import CalcBond_Batch
import interfaces_save
import connect_to_oracle
import acct_conditions, market_conditions,market_batch_conditions


# 批量接口
postUrl = 'http://191.168.6.6:8180/xalms/engine/calc.action'
postUrl_batch = 'http://191.168.6.6:8180/xalms/engine/calcBatch.action'

payloadHeader = {
    'Host': '191.168.6.6:8180',
    'Content-Type': 'application/json',
}
# 下载超时
timeOut = 250

host = '191.168.6.6'
port = '1521'
dbname = 'xalms'
username = 'xalms_trd'
password = 'xpar'

db = connect_to_oracle.DataBase(host, port, dbname, username, password)


if __name__ == '__main__':
    header_data = payloadHeader
    # instrumentList = [{'iCode': '000300', 'aType': 'IDX_S', 'mType': 'XSHG'},
    #                   {'iCode': '000016', 'aType': 'IDX_S', 'mType': 'XSHG'}]
    begDate = '2019-06-01'
    endDate = '2019-06-30'
    valueDate = '2019-06-30'
    sampleLenth = '0'

    instrumentList = [{'iCode': '151098', 'aType': 'SPT_BD', 'mType': 'XSHG'},
                      {'iCode': '151096', 'aType': 'SPT_BD', 'mType': 'XSHG'}]
    iCode = '151098'
    aType = 'SPT_BD'
    mType = 'XSHG'
    instrument = {'iCode': '151098',
                  'aType': 'SPT_BD',
                  'mType': 'XSHG'}
    interface_bond_batch = CalcBond_Batch(postUrl_batch, header_data, instrumentList, valueDate)
    # interface_bond = CalcBond(postUrl, header_data, iCode, aType, mType, valueDate)
    interfaces_data, res = interface_bond_batch.result()
    resultList = json.loads(res.text)
    # interfaces_save.result_save(instrument, resultList, excelname='CalcBond', sheetname='CalcBond')
    interfaces_save.batch_result_save(instrumentList, resultList, excelname='CalcBond', sheetname='CalcBond')

