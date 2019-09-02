# coding = utf-8
import json
import requests


class CalcPaymentForReal(object):
    def __init__(self, postUrl, header_data, iCode, aType, mType, valueDate, streamID, fixingType, isInTrade):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcPaymentForReal'
        self.iCode = iCode
        self.aType = aType
        self.mType = mType
        self.valueDate = valueDate
        self.streamID = streamID
        self.fixingType = fixingType
        self.isInTrade = isInTrade

    def result(self):
        interfaces_data = {
            "method": self.method,
            "iCode": self.iCode,
            "aType": self.aType,
            "mType": self.mType,
            "valueDate": self.valueDate,
            "streamID": self.streamID,
            "fixingType": self.fixingType,
            "isInTrade": self.isInTrade,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcPayment(object):
    def __init__(self, postUrl, header_data, iCode, aType, mType):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcPayment'
        self.iCode = iCode
        self.aType = aType
        self.mType = mType

    def result(self):
        interfaces_data = {
            "method": self.method,
            "iCode": self.iCode,
            "aType": self.aType,
            "mType": self.mType,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result

