# coding = utf-8
import json
import requests


class CalcCVTBondForReal(object):
    def __init__(self, postUrl, header_data, iCode, aType, mType, valueDate, AIOffset, price, priceType, bondPrice, bondPriceType, stockDividendRate, stockPrice):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcCVTBondForReal'
        self.iCode = iCode
        self.aType = aType
        self.mType = mType
        self.valueDate = valueDate
        self.AIOffset = AIOffset
        self.price = price
        self.priceType = priceType
        self.bondPrice = bondPrice
        self.bondPriceType = bondPriceType
        self.stockDividendRate = stockDividendRate
        self.stockPrice = stockPrice

    def result(self):
        interfaces_data = {
            "method": self.method,
            "iCode": self.iCode,
            "aType": self.aType,
            "mType": self.mType,
            "valueDate": self.valueDate,
            "AIOffset": self.AIOffset,
            "price": self.price,
            "priceType": self.priceType,
            "bondPrice": self.bondPrice,
            "bondPriceType": self.bondPriceType,
            "stockDividendRate": self.stockDividendRate,
            "stockPrice": self.stockPrice,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result
