# coding = utf-8
import json
import requests


class BrinsonAttr(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, begDate, endDate, bCode):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'brinsonAttr'
        self.portCode = portCode
        self.nodeId = nodeId
        self.begDate = begDate
        self.endDate = endDate
        self.bCode = bCode

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "begDate": self.begDate,
            "endDate": self.endDate,
            "bCode": self.bCode,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result
