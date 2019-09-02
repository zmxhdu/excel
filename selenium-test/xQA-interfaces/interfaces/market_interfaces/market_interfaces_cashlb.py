# coding = utf-8
import json
import requests


class CalcLBSForReal(object):
    def __init__(self, postUrl, header_data, bondList):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcLBSForReal'
        self.bondList = bondList

    def result(self):
        interfaces_data = {
            "method": self.method,
            "bondList": self.bondList,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcLBS(object):
    def __init__(self, postUrl, header_data, bondList):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcLBS'
        self.bondList = bondList

    def result(self):
        interfaces_data = {
            "method": self.method,
            "bondList": self.bondList,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class RunIRStreamsTask(object):
    def __init__(self, postUrl, header_data, instrumentList, valueDate):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'runIRStreamsTask'
        self.instrumentList = instrumentList
        self.valueDate = valueDate

    def result(self):
        interfaces_data = {
            "method": self.method,
            "bondList": self.instrumentList,
            "valueDate": self.valueDate
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result
