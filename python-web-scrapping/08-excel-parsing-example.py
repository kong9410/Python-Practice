#08-excel-parsing-example
import xlrd

wb = xlrd.open_workbook("kbo_rank.xlsx")
ws = wb.sheet_by_index(0)

print(wb.sheet_names())
print(ws.cell_value(1,1))
print(ws.col_values(1)[1])
print(ws.col_values(1)[2])
print(ws.row_values(0)[1])
print(ws.row_values(0)[2])

# 행, 열 수 세기
nrow = ws.nrows
ncol = ws.ncols
print(nrow)
print(ncol)
