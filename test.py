# coding = utf-8

import pandas as pd
import os

# file = os.getcwd()+'\\tmp001.xlsx'
x1 = pd.read_excel('tmp001.xlsx')
# print(x1['T_DATE'], x1['PF_RETURN'])
x2 = x1.loc[:,['T_DATE','PF_RETURN']][(x1['T_DATE']>='2014-10-10')&(x1['T_DATE']<='2014-10-20')]
# x2 = x1.loc[:,['T_DATE','PF_RETURN']][(x1['T_DATE']>='2014-10-08')&(x1['T_DATE']<='2014-10-20')]

x2['标准差'] = '=stdev(C%d:C%d)' %(2, x2['PF_RETURN'].count()+5)
x2['累计收益率'] = '=PRODUCT(C2:C12+1)-1'
x2 = x2.reset_index()
del x2['index']
x2.ix[1:, '标准差'] = ""
x2.ix[1:, '累计收益率'] = ""


out = pd.ExcelWriter('out.xlsx')
x2.to_excel(out)
out.save()
# print(x2['PF_RETURN'].var()*100)
