from openpyxl import Workbook

wb = Workbook()  #새 워크북 생성 : 엑셀파일 열었음 
ws = wb.active   #현재 활성화된 Excel Sheet 가져옴 
ws.title = "OKOK"  #Sheet의 이름을 변경 
wb.save("test.xlsx")
wb.close()