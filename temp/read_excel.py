#1.导入xlrd
import xlrd
from conf import config

#2.打开excel（work_book）
excel = xlrd.open_workbook(config.data_file)

#3.指定工作表

sheet = excel.sheet_loaded("登录")
sheet = excel.sheet_by_index(0)

#4.读取信息
#print(sheet.nrows)#有效数据行数
#print(sheet.ncols)#有效数据列数

#print(sheet.row_values(0))#打印第一行数据
#print(sheet.row_values(1))#打印地二行数据

#print(sheet.cell(1,0).value)#打印指定单元格数据


#练习1: 打印注册模块的用例，不要标题行

#sheet1 = excel.sheet_by_name("注册")
#for data in range(1,sheet1.nrows):
#     print(sheet1.row_values(data))

#练习2
def case_data(sheet,casename):
    sheet2 = excel.sheet_by_name(sheet)
    data = sheet2.row_values(casename)
    return  data

getdata = case_data("注册","test_user_reg_normal")
