# coding = utf-8
import json
import requests


class CalcAcctPerformance(object):
    def __init__(self, postUrl, header_data, portCode, list, begDate, endDate):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcAcctPerformance'
        self.portCode = portCode
        self.list = list
        self.begDate = begDate
        self.endDate = endDate

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "list": self.list,
            "begDate": self.begDate,
            "endDate": self.endDate,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class AcctPerfSerial(object):
    def __init__(self, postUrl, header_data, portCode, list, begDate, endDate):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'acctPerfSerial'
        self.portCode = portCode
        self.list = list
        self.begDate = begDate
        self.endDate = endDate

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "list": self.list,
            "begDate": self.begDate,
            "endDate": self.endDate,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcPortRiskAdjustIndex(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, begData, endDate, sampleLenth, calcPeriodFrequencyType,
                 alpha, isYeared, riskFreeRateID, rtnType, benchID, list):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcPortRiskAdjustIndex'
        self.portCode = portCode
        self.nodeId = nodeId
        self.begData = begData
        self.endDate = endDate
        self.sampleLenth = sampleLenth
        self.calcPeriodFrequencyType = calcPeriodFrequencyType
        self.alpha = alpha
        self.isYeared = isYeared
        self.riskFreeRateID = riskFreeRateID
        self.rtnType = rtnType
        self.benchID = benchID
        self.list = list

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "begData": self.begData,
            "endDate": self.endDate,
            "sampleLenth": self.sampleLenth,
            "calcPeriodFrequencyType": self.calcPeriodFrequencyType,
            "alpha": self.alpha,
            "isYeared": self.isYeared,
            "riskFreeRateID": self.riskFreeRateID,
            "rtnType": self.rtnType,
            "benchID": self.benchID,
            "list": self.list,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result
