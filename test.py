# coding = utf-8

import pandas as pd


x1 = pd.read_excel('E:\Python\练习\excel\\tmp001.xlsx')
# print(x1['T_DATE'], x1['PF_RETURN'])
x2 = x1.loc[:,['T_DATE','PF_RETURN']][(x1['T_DATE']>='2014-10-10')&(x1['T_DATE']<='2014-10-20')]
# x2 = x1.loc[:,['T_DATE','PF_RETURN']][(x1['T_DATE']>='2014-10-08')&(x1['T_DATE']<='2014-10-20')]

x2['var'] = x2['PF_RETURN'].var()
x2 = x2.reset_index()
del x2['index']
x2.ix[1:, 'var'] = ""

out = pd.ExcelWriter('E:\Python\练习\excel\\out.xlsx')
x2.to_excel(out)
out.save()
# print(x2['PF_RETURN'].var()*100)
