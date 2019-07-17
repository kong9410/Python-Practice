#09-create-xls-file
import xlwt, xlrd

wb=xlwt.Workbook(encoding='utf-8')
ws=wb.add_sheet('sheet1')

ws.write(0,0, "순위")
ws.write(0,1, "이름")
ws.write(1,0, "1")
ws.write(1,1, "Ronaldo")
ws.write(2,0, "2")
ws.write(2,1, "Rashford")
ws.write(3,0, "3")
ws.write(3,1, "lsco")

wb.save('player.xls')
