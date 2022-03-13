from openpyxl import Workbook
from openpyxl.utils.cell import coordinate_from_string
import random

wb = Workbook()
ws = wb.active

ws.append(["#", "English","Math"])
for i in range(1,11):
  ws.append([i, random.randint(0,100),random.randint(0,100)])

scores = ws[2:ws.max_row]
for score in scores:
  for cell in score:
    #print(cell.value, end=" ")
    #print(cell.coordinate, end=" ")
    xy = coordinate_from_string(cell.coordinate)
    print("column=", xy[0])
    
  print()

wb.save("test.xlsx")
wb.close