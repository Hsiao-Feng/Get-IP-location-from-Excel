from qqwry import QQwry
import openpyxl
num = 100 #查询的总行数
file = 'ip.xlsx' #文件名，需要在同一目录下
key = 0 #0=只显示地区（如广东省深圳市），1=只显示详细地址（如某某网吧）
q = QQwry()
q.load_file('qqwry.dat')
row = 1
while row<=num:
    print(q.lookup(openpyxl.load_workbook(file)['Sheet1'].cell(row=row,column=1).value)[key])
    row += 1
