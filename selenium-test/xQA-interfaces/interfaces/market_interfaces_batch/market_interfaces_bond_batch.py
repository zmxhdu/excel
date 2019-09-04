# coding = utf-8
import json
import requests


class CalcBondForReal_Batch(object):
    def __init__(self, postUrl, header_data, bondList):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcBondForReal'
        self.bondList = bondList

    def result(self):
        interfaces_data = {
            "method": self.method,
            "bondList": self.bondList,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcBond_Batch(object):
    def __init__(self, postUrl, header_data, instrumentList, valueDate):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcBond'
        self.instrumentList = instrumentList
        self.valueDate = valueDate

    def result(self):
        interfaces_data = {
            "method": self.method,
            "instrumentList": self.instrumentList,
            "valueDate": self.valueDate
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result
