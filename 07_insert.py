from openpyxl import load_workbook

wb = load_workbook("./test.xlsx")
ws = wb.active

ws.insert_cols(2,5) 

wb.save("test.xlsx")
wb.close()