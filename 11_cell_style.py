from openpyxl import load_workbook
from openpyxl.styles import Font, Border, Side

wb = load_workbook("./test.xlsx")
ws = wb.active

a1 = ws["A1"]
b1 = ws["B1"]
c1 = ws["C1"]

ws.column_dimensions["A"].width = 5
ws.row_dimensions[1].height = 50

a1.font = Font(color="FF0000", italic=True, bold=True)
b1.font = Font(color="CC33FF", name="Arial", strike=True)
c1.font = Font(color="0000FF", size=20, underline="double")

title_border = Border(left=Side(style="thin"), right=Side(style="thin"), top=Side(style="thin"), bottom=Side(style="thin"))
a1.border = title_border
b1.border = title_border
c1.border = title_border

wb.save("new.xlsx")
wb.close()

 