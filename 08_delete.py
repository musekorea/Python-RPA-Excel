from openpyxl import load_workbook

wb = load_workbook("test.xlsx")
ws = wb.active

ws.delete_cols(2,6)
wb.save("test.xlsx")
wb.close()