# coding = utf-8
import json
import market_interfaces
import acct_interfaces
from market_interfaces_batch import market_interfaces_bond_batch, market_interfaces_fund_batch, \
    market_interfaces_stock_batch, market_interfaces_tidx_batch
from market_interfaces import market_interfaces_tidx, market_interfaces_bond, market_interfaces_bondfutuer, \
    market_interfaces_cashlb, market_interfaces_cvtbond, market_interfaces_fund, market_interfaces_payment, \
    market_interfaces_stock, market_interfaces_stockidxfutuer, market_interfaces_stockoption, market_interfaces_tirswap
from acct_interfaces import acct_interfaces_brinson, acct_interfaces_hld, acct_interfaces_liquid, acct_interfaces_market, acct_interfaces_return
import interfaces_save
from interfaces_conditions import acct_conditions, market_conditions
import configparser


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.config')
    postUrl = config.get('POST', 'postUrl')
    postUrl_batch = config.get('POST', 'postUrl_batch')
    payloadHeader = json.loads(config.get('POST', 'payloadHeader'))

    header_data = payloadHeader
    begDate = '2019-06-01'
    endDate = '2019-06-30'
    valueDate = '2019-06-30'
    sampleLenth = '0'

    iCode = '151098'
    aType = 'SPT_BD'
    mType = 'XSHG'
    instrument = {'iCode': '151098',
                  'aType': 'SPT_BD',
                  'mType': 'XSHG'}
    instrumentList = market_conditions.Market_Conditions().get_sql('TBND_BATCH')
    interface_bond_batch = market_interfaces_bond_batch.CalcBondForReal_Batch(postUrl_batch, header_data, instrumentList)

    # interface_bond = CalcBond(postUrl, header_data, iCode, aType, mType, valueDate)
    interfaces_data, res = interface_bond_batch.result()
    resultList = json.loads(res.text)
    # interfaces_save.result_save(instrument, resultList, excelname='CalcBond', sheetname='CalcBond')
    # interfaces_save.batch_result_save(instrumentList, resultList, excelname='CalcBond', sheetname='CalcBond')
    interfaces_save.batch_result_save(instrumentList, resultList, excelname='TIDX.xlsx', sheetname='TIDX')
