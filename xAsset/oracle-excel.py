# coding = utf-8

import cx_Oracle
import xlsxwriter


db = cx_Oracle.connect('xasset_0100/xrisk@XRISK_73')

cursor = db.cursor()
x = cursor.execute("select * from TPRT where PORT_CODE='SB9021'")
title = [i[0] for i in cursor.description]
print(x.fetchall())
for i in title:
    print(i, end=' ')


wb = xlsxwriter.Workbook('持仓.xlsx')
ws = wb.add_worksheet()
