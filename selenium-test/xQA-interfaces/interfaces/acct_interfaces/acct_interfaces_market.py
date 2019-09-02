# coding = utf-8
import json
import requests


class CalcAnteBeta(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, bookCurrency,  peCode, Lambda, sampleDays, benchIndex, isCalcSingleBeta, list):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcAnteBeta'
        self.portCode = portCode
        self.nodeId = nodeId
        self.tDate = tDate
        self.bookCurrency = bookCurrency
        self.peCode = peCode
        self.Lambda = Lambda
        self.sampleDays = sampleDays
        self.benchIndex = benchIndex
        self.isCalcSingleBeta = isCalcSingleBeta
        self.list = list

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "tDate": self.tDate,
            "bookCurrency": self.bookCurrency,
            "peCode": self.peCode,
            "lambda": self.Lambda,
            "sampleDays": self.sampleDays,
            "benchIndex": self.benchIndex,
            "isCalcSingleBeta": self.isCalcSingleBeta,
            "list": self.list,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcAnteBetaJ(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, peCode, Lambda, sampleDays, benchIndex, list):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcAnteBetaJ'
        self.portCode = portCode
        self.nodeId = nodeId
        self.tDate = tDate
        self.peCode = peCode
        self.Lambda = Lambda
        self.sampleDays = sampleDays
        self.benchIndex = benchIndex
        self.list = list

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "tDate": self.tDate,
            "peCode": self.peCode,
            "lambda": self.Lambda,
            "sampleDays": self.sampleDays,
            "benchIndex": self.benchIndex,
            "list": self.list,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcAnteVar(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, bookCurrency, peCode, confidence, Lambda, horizon,
                 methodType, pathNum, horizonMethodType, sampleDays, list):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcAnteVar'
        self.portCode = portCode
        self.nodeId = nodeId
        self.tDate = tDate
        self.bookCurrency = bookCurrency
        self.peCode = peCode
        self.confidence = confidence
        self.Lambda = Lambda
        self.horizon = horizon
        self.methodType = methodType
        self.pathNum = pathNum
        self.horizonMethodType = horizonMethodType
        self.sampleDays = sampleDays
        self.list = list

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "tDate": self.tDate,
            "bookCurrency": self.bookCurrency,
            "peCode": self.peCode,
            "confidence": self.confidence,
            "lambda": self.Lambda,
            "horizon": self.horizon,
            "methodType": self.methodType,
            "pathNum": self.pathNum,
            "horizonMethodType": self.horizonMethodType,
            "sampleDays": self.sampleDays,
            "list": self.list,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcAnteVarJ(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, peCode, confidence, Lambda, horizon,
                 methodType, horizonMethodType, sampleDays, list):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcAnteVarJ'
        self.portCode = portCode
        self.nodeId = nodeId
        self.tDate = tDate
        self.peCode = peCode
        self.confidence = confidence
        self.Lambda = Lambda
        self.horizon = horizon
        self.methodType = methodType
        self.horizonMethodType = horizonMethodType
        self.sampleDays = sampleDays
        self.list = list

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "tDate": self.tDate,
            "peCode": self.peCode,
            "confidence": self.confidence,
            "lambda": self.Lambda,
            "horizon": self.horizon,
            "methodType": self.methodType,
            "horizonMethodType": self.horizonMethodType,
            "sampleDays": self.sampleDays,
            "list": self.list,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcAnteBenchVar(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, bookCurrency, peCode, confidence, Lambda, horizon,
                 methodType, pathNum, horizonMethodType, sampleDays):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcAnteBenchVar'
        self.portCode = portCode
        self.nodeId = nodeId
        self.tDate = tDate
        self.bookCurrency = bookCurrency
        self.peCode = peCode
        self.confidence = confidence
        self.Lambda = Lambda
        self.horizon = horizon
        self.methodType = methodType
        self.pathNum = pathNum
        self.horizonMethodType = horizonMethodType
        self.sampleDays = sampleDays

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "tDate": self.tDate,
            "bookCurrency": self.bookCurrency,
            "peCode": self.peCode,
            "confidence": self.confidence,
            "lambda": self.Lambda,
            "horizon": self.horizon,
            "methodType": self.methodType,
            "pathNum": self.pathNum,
            "horizonMethodType": self.horizonMethodType,
            "sampleDays": self.sampleDays,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcAnteBenchVarJ(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, peCode, confidence, Lambda, horizon,
                 methodType, horizonMethodType, sampleDays):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcAnteBenchVarJ'
        self.portCode = portCode
        self.nodeId = nodeId
        self.tDate = tDate
        self.peCode = peCode
        self.confidence = confidence
        self.Lambda = Lambda
        self.horizon = horizon
        self.methodType = methodType
        self.horizonMethodType = horizonMethodType
        self.sampleDays = sampleDays

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "tDate": self.tDate,
            "peCode": self.peCode,
            "confidence": self.confidence,
            "lambda": self.Lambda,
            "horizon": self.horizon,
            "methodType": self.methodType,
            "horizonMethodType": self.horizonMethodType,
            "sampleDays": self.sampleDays,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result

class CalcAnteStd(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, bookCurrency, peCode, sampleDays, Lambda, list):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcAnteStd'
        self.portCode = portCode
        self.nodeId = nodeId
        self.tDate = tDate
        self.bookCurrency = bookCurrency
        self.peCode = peCode
        self.sampleDays = sampleDays
        self.Lambda = Lambda
        self.list = list

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "tDate": self.tDate,
            "bookCurrency": self.bookCurrency,
            "peCode": self.peCode,
            "sampleDays": self.sampleDays,
            "lambda": self.Lambda,
            "list": self.list,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result

class CalcAnteStdJ(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, peCode, sampleDays, Lambda, list):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcAnteStd'
        self.portCode = portCode
        self.nodeId = nodeId
        self.tDate = tDate
        self.peCode = peCode
        self.sampleDays = sampleDays
        self.Lambda = Lambda
        self.list = list

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "tDate": self.tDate,
            "peCode": self.peCode,
            "sampleDays": self.sampleDays,
            "lambda": self.Lambda,
            "list": self.list,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result

class InterestRisk(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, qSource, list):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'interestRisk'
        self.portCode = portCode
        self.nodeId = nodeId
        self.tDate = tDate
        self.qSource = qSource
        self.list = list

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "tDate": self.tDate,
            "qSource": self.qSource,
            "list": self.list,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result

class MarketRiskStock(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, qSource, list):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'marketRiskStock'
        self.portCode = portCode
        self.nodeId = nodeId
        self.tDate = tDate
        self.qSource = qSource
        self.list = list

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "tDate": self.tDate,
            "qSource": self.qSource,
            "list": self.list,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result

class EquityRisk(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, list):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'equityRisk'
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


class CalcPercentVar(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, bookCurrency, peCode, confidence, Lambda, horizon,
                 methodType, pathNum, horizonMethodType, sampleDays):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcPercentVar'
        self.portCode = portCode
        self.nodeId = nodeId
        self.tDate = tDate
        self.bookCurrency = bookCurrency
        self.peCode = peCode
        self.confidence = confidence
        self.Lambda = Lambda
        self.horizon = horizon
        self.methodType = methodType
        self.pathNum = pathNum
        self.horizonMethodType = horizonMethodType
        self.sampleDays = sampleDays

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "tDate": self.tDate,
            "bookCurrency": self.bookCurrency,
            "peCode": self.peCode,
            "confidence": self.confidence,
            "lambda": self.Lambda,
            "horizon": self.horizon,
            "methodType": self.methodType,
            "pathNum": self.pathNum,
            "horizonMethodType": self.horizonMethodType,
            "sampleDays": self.sampleDays,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcPercentVarJ(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, peCode, confidence, Lambda, horizon,
                 methodType, horizonMethodType, sampleDays):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcPercentVarJ'
        self.portCode = portCode
        self.nodeId = nodeId
        self.tDate = tDate
        self.peCode = peCode
        self.confidence = confidence
        self.Lambda = Lambda
        self.horizon = horizon
        self.methodType = methodType
        self.horizonMethodType = horizonMethodType
        self.sampleDays = sampleDays

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "tDate": self.tDate,
            "peCode": self.peCode,
            "confidence": self.confidence,
            "lambda": self.Lambda,
            "horizon": self.horizon,
            "methodType": self.methodType,
            "horizonMethodType": self.horizonMethodType,
            "sampleDays": self.sampleDays,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class FundHoldCount(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, list):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'fundHoldCount'
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

class CalcAnteTe(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, bookCurrency, peCode, Lambda, sampleDays, benchIndex, list):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcAnteTe'
        self.portCode = portCode
        self.nodeId = nodeId
        self.tDate = tDate
        self.bookCurrency = bookCurrency
        self.peCode = peCode
        self.Lambda = Lambda
        self.sampleDays = sampleDays
        self.benchIndex = benchIndex
        self.list = list

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "tDate": self.tDate,
            "bookCurrency": self.bookCurrency,
            "peCode": self.peCode,
            "lambda": self.Lambda,
            "sampleDays": self.sampleDays,
            "benchIndex": self.benchIndex,
            "list": self.list,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result


class CalcAnteTeJ(object):
    def __init__(self, postUrl, header_data, portCode, nodeId, tDate, peCode, Lambda, sampleDays,
                 benchIndex, list):
        self.postUrl = postUrl
        self.header_data = header_data
        self.method = 'calcAnteTeJ'
        self.portCode = portCode
        self.nodeId = nodeId
        self.tDate = tDate
        self.peCode = peCode
        self.Lambda = Lambda
        self.sampleDays = sampleDays
        self.benchIndex = benchIndex
        self.list = list

    def result(self):
        interfaces_data = {
            "method": self.method,
            "portCode": self.portCode,
            "nodeId": self.nodeId,
            "tDate": self.tDate,
            "peCode": self.peCode,
            "lambda": self.Lambda,
            "sampleDays": self.sampleDays,
            "benchIndex": self.benchIndex,
            "list": self.list,
        }

        result = requests.post(self.postUrl, data=json.dumps(interfaces_data), headers=self.header_data)

        return interfaces_data, result