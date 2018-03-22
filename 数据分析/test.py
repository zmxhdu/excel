# coding = utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# %matplotlib inline  # ipython魔法函数
plt.style.use('ggplot')

df = pd.read_csv("DataAnalyst.csv", encoding='gb2312')

# 根据 positionId 去重
df_duplicates = df.drop_duplicates(subset='positionId', keep='first')


# 获取薪资上下限
def cut_word(word, method):
    position = word.find('-')
    length = len(word)
    if position != -1:
        bottomSalary = word[:position-1]
        topSalary = word[position + 1:length - 1]
    else:
        bottomSalary = word[:word.upper().find('K')]
        topSalary = bottomSalary
    if method == 'bottom':
        return bottomSalary
    else:
        return topSalary


df_duplicates = df_duplicates.copy()  # copy下，防止警告SettingWithCopyWarning
df_duplicates['bottomSalary'] = df_duplicates.salary.apply(cut_word, method='bottom')
df_duplicates['topSalary'] = df_duplicates.salary.apply(cut_word, method='top')

# 转换成 int 格式
df_duplicates.bottomSalary = df_duplicates.bottomSalary.astype('int')
df_duplicates.topSalary = df_duplicates.topSalary.astype('int')

# 计算平均工资
df_duplicates['avgSalary'] = df_duplicates.apply(lambda x: (x.bottomSalary+x.topSalary)/2, axis=1)

df_clean = df_duplicates[['city', 'companyShortName', 'companySize', 'education', 'positionName', 'positionLables',
                          'workYear', 'bottomSalary', 'topSalary', 'avgSalary']]

# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)

plt.hist(df_clean.avgSalary, bins=15)
plt.show()
