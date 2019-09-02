# coding = utf-8
import json
import requests


class CalcAcctHold(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, nodePid, list):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcAcctHold'
        self.portCode = portCode
        self.nodeId = nodeId
        self.tDate = tDate
        self.nodePid = nodePid
        self.list = list

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "tDate": self.tDate,
            "nodePid": self.nodePid,
            "list": self.list,

        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcAcctHoldSegment(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, begDate, endDate, list):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcAcctHoldSegment'
        self.portCode = portCode
        self.nodeId = nodeId
        self.begDate = begDate
        self.endDate = endDate
        self.list = list

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "begDate": self.begDate,
            "endDate": self.endDate,
            "list": self.list,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class TcrpHldPlService(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, list):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'tcrpHldPlService'
        self.portCode = portCode
        self.nodeId = nodeId
        self.tDate = tDate
        self.list = list

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "tDate": self.tDate,
            "list": self.list,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result
