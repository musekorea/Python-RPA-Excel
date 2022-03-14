from openpyxl import Workbook
from openpyxl.utils.cell import coordinate_from_string
import random

wb = Workbook()
ws = wb.active

ws.append(["#", "English","Math"])
for i in range(1,11):
  ws.append([i, random.randint(0,100),random.randint(0,100)])

for row in ws.iter_rows(min_row=1, max_row=5, min_col=1, max_col=1):
  print(row)
  



#wb.save("test.xlsx")
wb.close