import requests
import os
import xlrd
from selenium import webdriver
def save_photo(root, url):
    if not os.path.exists(root):
        os.makedirs(root)
    m = url.split("&")[3] + ".jpg"#把经纬度和方向作为街景的名称
    name = root + m
    r = requests.get(url)
    with open(name, "wb") as f:
        f.write(r.content)
        f.close()
if __name__ == '__main__':
    workbook = xlrd.open_workbook('F:/location_shift/01.xlsx')
    sheet1 = workbook.sheet_by_index(0)
    xx=sheet1.nrows
    yy=sheet1.ncols
    x=0
    y=0
    while x < xx:
      while y < yy:
        location = str(sheet1.cell(x,0).value)
        a = webdriver.Chrome()
        url = "http://api.map.baidu.com/panorama/v2?ak=u2Og91O2kRkgXLbHQGCLnP2pp3G5Nu5N&width=512&height=256&location=" + location + "&fov=360"
        root = "F://view_final//"  # 文件保存位置
        save_photo(root,url)
        a.quit()
        x += 1
      y = 0
    print("选择的街景已保存")