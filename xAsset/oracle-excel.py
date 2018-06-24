# coding = utf-8

import cx_Oracle
import xlsxwriter


db = cx_Oracle.connect('xasset_0100/xrisk@XRISK_73')

cursor = db.cursor()
cursor.prepare('select P_ID,T_DATE,PF_MTM,PF_PRE_MTM,PF_CF_IN,PF_CF_OUT,PF_RETURN,PF_TW_RETURN '
               'from TBSI_ACCT '
               'where P_ID in (select P_ID from TPRT where PORT_CODE=:PORT_CODE and P_TYPE=:P_TYPE) '
               'and T_DATE>=:BEG_DATE and T_DATE<=:END_DATE')
x = cursor.execute(None, {'PORT_CODE': 'SB9021', 'P_TYPE': '12', 'BEG_DATE': '2017-12-12', 'END_DATE': '2017-12-18'})
title = [i[0] for i in cursor.description]
result = x.fetchall()


print(result)



wb = xlsxwriter.Workbook('组合.xlsx')
ws = wb.add_worksheet()


# 字段名
col = 0
for i in title:
    ws.write(0, col, i)
    col += 1


# 数据
row = 1
for m in result:
    col = 0
    for n in m:
        print(row, col, n)
        ws.write(row, col, n)
        col += 1
    row += 1

# 写入公式
