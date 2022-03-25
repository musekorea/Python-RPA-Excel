from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws  = wb.active

img = Image("./wechat.png")
img.width = 30
img.height = 30
ws.add_image(img, "C3")

wb.save("new.xlsx")
wb.close()