# coding = utf-8
import json
import requests


class CalcTidxForReal_Batch(object):
    def __init__(self, postUrl, header_data, instrumentList, begDate, endDate, sampleLenth,
                 benchID='', riskFreeRateID='', calcPeriodFrequencyType='D'):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcTidxForReal'
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
            "riskFreeRateID": self.riskFreeRateID,
            "calcPeriodFrequencyType": self.calcPeriodFrequencyType
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcTidxInvlForReal_Batch(object):
    def __init__(self, postUrl, header_data, instrumentList, begDate, endDate, sampleLenth):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcTidxInvlForReal'
        self.instrumentList = instrumentList
        self.begDate = begDate
        self.endDate = endDate
        self.sampleLenth = sampleLenth

    def result(self):
        interfaces_data = {
            "method": self.method,
            "instrumentList": self.instrumentList,
            "begDate": self.begDate,
            "endDate": self.endDate,
            "sampleLenth": self.sampleLenth,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcTidx_Batch(object):
    def __init__(self, postUrl, header_data, instrumentList, valueDate):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcTidx'
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
