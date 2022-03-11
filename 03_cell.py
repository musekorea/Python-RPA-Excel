from openpyxl import Workbook
import random

wb = Workbook()
ws  = wb.active
ws.title = "CELL TEST"

for row in range(1,11):
  for col in range(1,8):
    ws.cell(row=row, column=col).value = random.randint(0,100)

wb.save("test.xlsx")
wb.close()
