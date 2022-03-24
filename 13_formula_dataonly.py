from openpyxl import load_workbook

wb = load_workbook("new.xlsx", data_only=True)
ws = wb.active

for row in ws.values:
  for value in row: 
    print(value)

wb.close()