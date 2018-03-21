# coding = utf-8

import openpyxl
import cx_Oracle
import xlsxwriter

username = 'xrisk'
password = 'xrisk'
ip = '127.0.0.1'
port = '1521'
databasename = 'orcl'
dsn = cx_Oracle.makedsn(ip, port, databasename)
db = cx_Oracle.connect(username, password, dsn)

cursor = db.cursor()


cursor.prepare('select P_ID,T_DATE,PF_MTM,PF_PRE_MTM,PF_CF_IN,PF_CF_OUT,PF_RETURN,PF_TW_RETURN from TBSI_ACCT where P_ID=:P_ID and T_DATE>=:BEG_DATE and T_DATE<=:END_DATE')
result = cursor.execute(None, {'P_ID':29, 'BEG_DATE':'2014-05-05', 'END_DATE':'2014-05-15'})
title = [i[0] for i in cursor.description]

print(result.fetchone(),title)
