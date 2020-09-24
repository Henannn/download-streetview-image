import requests
import xlrd
from selenium import webdriver
if __name__ == '__main__':
    workbook = xlrd.open_workbook('F:/location_shift/DL_WGS.xlsx')
    sheet1 = workbook.sheet_by_index(0)
    xx = sheet1.nrows
    yy = sheet1.ncols
    x = 0
    y = 0
    while x < xx:
        while y < yy:
            heng = sheet1.cell(x, 0).value
            shu = sheet1.cell(x, 1).value
            a = webdriver.Chrome()
            url = "http://api.map.baidu.com/ag/coord/convert?from=0&to=4&x=" + str(heng) + "&y=" + str(shu)
            r = requests.get(url)
            m = r.content
            print(m)
            a.close()
            x += 1
        y = 0


