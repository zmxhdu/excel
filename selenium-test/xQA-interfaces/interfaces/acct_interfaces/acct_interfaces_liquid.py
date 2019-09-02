# coding = utf-8
import json
import requests


class CalcAcctShareRatio(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, focusNum, priceType, nodePid, list):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcAcctShareRatio'
        self.portCode = portCode
        self.nodeId = nodeId
        self.tDate = tDate
        self.focusNum = focusNum
        self.priceType = priceType
        self.nodePid = nodePid
        self.list = list

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "tDate": self.tDate,
            "focusNum": self.focusNum,
            "priceType": self.priceType,
            "nodePid": self.nodePid,
            "list": self.list,

        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcAcctClassifyRatioJ(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, focusNum, priceType, nodePid, gCode, list):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcAcctClassifyRatioJ'
        self.portCode = portCode
        self.nodeId = nodeId
        self.tDate = tDate
        self.focusNum = focusNum
        self.priceType = priceType
        self.nodePid = nodePid
        self.gCode = gCode
        self.list = list

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "tDate": self.tDate,
            "focusNum": self.focusNum,
            "priceType": self.priceType,
            "nodePid": self.nodePid,
            "gCode": self.gCode,
            "list": self.list,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcAcctLiquidRatio(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, sampleDays, decRange, gainRatio, clearDays, list):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcAcctLiquidRatio'
        self.portCode = portCode
        self.nodeId = nodeId
        self.tDate = tDate
        self.sampleDays = sampleDays
        self.decRange = decRange
        self.gainRatio = gainRatio
        self.clearDays = clearDays
        self.list = list

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "tDate": self.tDate,
            "sampleDays": self.sampleDays,
            "decRange": self.decRange,
            "gainRatio": self.gainRatio,
            "clearDays": self.clearDays,
            "list": self.list,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result
