import base64
a=0
with open("F:/location_shift/DL_Decoding.txt","r", encoding='UTF-8') as f:
    #with open("F:/location_shift/location_y.txt", "w", encoding='UTF-8') as f1:
     for line in f.readlines():
      a=a+1
      if a <680:
          m = line.split('[')[2]
          n = base64.b64decode(m).decode("utf-8")
          o = line.split('"')[9]
          s = base64.b64decode(o).decode("utf-8")
          j = n + "," + s
          print (j)
