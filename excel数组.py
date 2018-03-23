# coding = utf-8

import openpyxl
import cx_Oracle
import xlsxwriter


def getconnoracle(username, password, ip, databasename):
    # username = 'xasset_0100'
    # password = 'xrisk'
    # ip = '191.168.0.73'
    port = '1521'  # 默认端口1521
    # databasename = 'xrisk'
    dsn = cx_Oracle.makedsn(ip, port, databasename)

    try :
        db = cx_Oracle.connect(username, password, dsn) # 连接数据库
        return db
    except Exception:
        print(Exception)


cursor = db.cursor()


cursor.prepare('select P_ID,T_DATE,PF_MTM,PF_PRE_MTM,PF_CF_IN,PF_CF_OUT,PF_RETURN,PF_TW_RETURN from TBSI_ACCT where P_ID=:P_ID and T_DATE>=:BEG_DATE and T_DATE<=:END_DATE')
result = cursor.execute(None, {'P_ID':29, 'BEG_DATE':'2014-05-05', 'END_DATE':'2014-05-15'})
title = [i[0] for i in cursor.description]

print(result.fetchall())
for i in title:
    print(i, end=' ')


# wb = xlsxwriter.Workbook('持仓.xlsx')
# ws = wb.add_worksheet()
# print(result.fetchone(),title)

def main():



if __name__ == '__main__':
    main()
