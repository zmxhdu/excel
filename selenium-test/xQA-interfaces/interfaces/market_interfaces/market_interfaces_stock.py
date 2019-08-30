# coding = utf-8
import json
import requests


class CalcStockForReal(object):
    def __init__(self, postUrl, header_data, instrumentList, begDate, endDate, sampleLenth,
                 benchID='', riskFreeRateID='', calcPeriodFrequencyType='D'):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcStockForReal'
        self.instrumentList = instrumentList
        self.begDate = begDate
        self.endDate = endDate
        self.sampleLenth = sampleLenth
        self.benchID = benchID
        self.riskFreeRateID = riskFreeRateID
        self.calcPeriodFrequencyType = calcPeriodFrequencyType

    def result(self):
        interfaces_data = {
            "method": self.method,
            "instrumentList": self.instrumentList,
            "begDate": self.begDate,
            "endDate": self.endDate,
            "sampleLenth": self.sampleLenth,
            "benchID": self.benchID,
            "riskFreeRateID": self.riskFreeRateID
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcStockInvlForReal(object):
    def __init__(self, postUrl, header_data, instrumentList, begDate, endDate, sampleLenth,
                 benchID='', riskFreeRateID='', calcPeriodFrequencyType='D'):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcStockInvlForReal'
        self.instrumentList = instrumentList
        self.begDate = begDate
        self.endDate = endDate
        self.sampleLenth = sampleLenth
        self.benchID = benchID
        self.riskFreeRateID = riskFreeRateID
        self.calcPeriodFrequencyType = calcPeriodFrequencyType

    def result(self):
        interfaces_data = {
            "method": self.method,
            "instrumentList": self.instrumentList,
            "begDate": self.begDate,
            "endDate": self.endDate,
            "sampleLenth": self.sampleLenth,
            "benchID": self.benchID,
            "riskFreeRateID": self.riskFreeRateID
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcStock(object):
    def __init__(self, postUrl, header_data, instrumentList, valueDate):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcStock'
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
