# coding = utf-8
import openpyxl


try:
    xALR_property_rules_wb = openpyxl.load_workbook('银保监发[2018]28号附件2-财产险.xlsx', read_only=True)  # 财产险校验规则
    xALR_life_rules_wb = openpyxl.load_workbook('银保监发[2018]28号附件3-人身险.xlsx', read_only=True)  # 人身险校验规则
except FileNotFoundError as rules_error:
    print(rules_error)
    exit()


# 需校验的财产险sheet名称列表
property_rules_sheets = ['表1-1 资产配置状况', '表1-2 资产信用状况', '表1-3 负债产品信息',
                         '表2-1 沉淀资金匹配（传统保险账户）', '表2-2 期限结构匹配（投资型和次级债账户）',
                         '表3-1 成本收益匹配状况', '表3-2 成本收益匹配压力测试',
                         '表4-1 现金流测试_普通账户', '表4-2 现金流测试_传统保险账户',
                         '表4-3 现金流测试_预定收益型投资保险产品账户', '表4-4 现金流测试_独立账户']

# 需校验的人身险sheet名称列表
life_rules_sheets = ['表1-1 资产配置状况', '表1-2 资产信用状况', '表1-3 负债产品信息',
                     '表2-1 期限结构匹配测试表_修正久期', '表2-2 期限结构匹配测试表_关键久期',
                     '表3-1 成本收益匹配状况表', '表3-2 成本收益匹配压力测试表',
                     '表4-1 现金流测试表_普通账户', '表4-2 现金流测试表_传统保险账户',
                     '表4-3 现金流测试表_分红保险账户', '表4-4 现金流测试表_万能保险账户', '表4-5 现金流测试表_独立账户']


# 判断报告类型是财产险还是人身险
def property_or_life_excle(filename):
    # TODO:增加判断“封面”是否存在
    sheet = filename['封面']

    if sheet['A6'].value == '财产保险公司资产负债管理量化评估表':
        print("待校验的报告类型是:", '财产险报告')
        xALR_property_rules_check(filename)
    elif sheet['A4'].value == '人身保险公司资产负债管理量化评估表':
        print("待校验的报告类型是:", '人身险报告')
        xALR_life_rules_check(filename)


# 财产险规则校验，蓝色单元格
def xALR_property_rules_check(filename):
    xALR_property_rules_sheets = xALR_property_rules_wb.sheetnames
    xALR_test_sheets = filename.sheetnames

    if xALR_test_sheets != xALR_property_rules_sheets:
        print("待检验文件sheet页不符合要求")
        print("需要以下sheet页:", xALR_property_rules_sheets)
        print("带校验文件只有以下sheet页:", xALR_test_sheets)
    else:
        for sheet in property_rules_sheets:
            for cells in xALR_property_rules_wb[sheet]:
                print(cells[1])


# 人身险规则校验，黄色单元格
def xALR_life_rules_check(filename):
    xALR_life_rules_sheets = xALR_life_rules_wb.sheetnames
    xALR_test_sheets = filename.sheetnames

    if xALR_test_sheets != xALR_life_rules_sheets:
        print("待检验文件sheet页不符合要求")
        print("需要以下sheet页:", xALR_life_rules_sheets)
        print("带校验文件只有以下sheet页:", xALR_test_sheets)


if __name__ == '__main__':
    try:
        file = '银保监发(2018)28号附件2_安信0629-财产险.xlsx'
        xALR_test_wb = openpyxl.load_workbook(file, read_only=True)
    except FileNotFoundError as file_error:
        print(file_error)
        exit()

    property_or_life_excle(xALR_test_wb)
