# coding = utf-8
import json
import requests


class CalcBondFuture(object):
    def __init__(self, postUrl, header_data, iCode, aType, mType, valueDate):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcBondFuture'
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
            "valueDate": self.valueDate,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result
