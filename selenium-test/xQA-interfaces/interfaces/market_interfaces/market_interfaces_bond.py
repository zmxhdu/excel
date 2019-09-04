# coding = utf-8
import json
import requests


class CalcBondForReal(object):
    def __init__(self, postUrl, header_data, iCode, aType, mType, valueDate, AIOffset, price, priceType):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcBondForReal'
        self.iCode = iCode
        self.aType = aType
        self.mType = mType
        self.valueDate = valueDate
        self.AIOffset = AIOffset
        self.price = price
        self.priceType = priceType

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
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcOEBondForReal(object):
    def __init__(self, postUrl, header_data, iCode, aType, mType, valueDate, AIOffset, price, priceType):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcOEBondForReal'
        self.iCode = iCode
        self.aType = aType
        self.mType = mType
        self.valueDate = valueDate
        self.AIOffset = AIOffset
        self.price = price
        self.priceType = priceType

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
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcBond(object):
    def __init__(self, postUrl, header_data, iCode, aType, mType, valueDate):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcBond'
        self.iCode = iCode
        self.aType = aType
        self.mType = mType
        self.valueDate = valueDate

    def result(self):
        interfaces_data = {
            "method": self.method,
            "iCode": self.iCode,
            "aType": self.aType,
            "mType": self.mType,
            "valueDate": self.valueDate
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result
