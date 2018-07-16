# coding = utf-8
import openpyxl


wb = openpyxl.load_workbook('银保监发(2018)28号附件2_安信0629-财产险.xlsx', read_only=True)
print(wb.sheetnames)