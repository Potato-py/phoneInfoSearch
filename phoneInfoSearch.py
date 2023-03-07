from phone import Phone
import xlrd
import xlwt
import sys

def getPhoneInfo():
    phoneFile = xlrd.open_workbook(sys.argv[1]).sheet_by_index(0)
    phoneInfoFileWt = xlwt.Workbook()
    phoneInfoFile = phoneInfoFileWt.add_sheet("sheet1")

    phoneFileRows = phoneFile.nrows

    phoneInfoFile.write(0, 0, u'电话号')
    phoneInfoFile.write(0, 1, u'省份')
    phoneInfoFile.write(0, 2, u'城市')
    phoneInfoFile.write(0, 3, u'区号')
    phoneInfoFile.write(0, 4, u'运营商')

    for i in range(0, phoneFileRows):
        print(phoneFile.cell_value(i, 0))
        try:
            Telvalue = int(phoneFile.cell_value(i, 0))
        except:
            print(phoneFile.cell_value(i, 0)+"not phoneNum,continue")
            phoneInfoFile.write(i + 1, 0, phoneFile.cell_value(i, 0)) # 给新表的各列添加对应的数据
            continue
        data = Phone().find(Telvalue)
        phoneInfoFile.write(i + 1, 0, Telvalue) # 给新表的各列添加对应的数据
        try:
            phoneInfoFile.write(i + 1, 1, data['province'])
            phoneInfoFile.write(i + 1, 2, data['city'])
            phoneInfoFile.write(i + 1, 3, data['area_code'])
            phoneInfoFile.write(i + 1, 4, data['phone_type'])
            phoneInfoFileWt.save(r'New_Tel.xls')
        except Exception as e:
            print("none")
            print(e)


getPhoneInfo()