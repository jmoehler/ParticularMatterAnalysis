import urllib
import datetime
import time

start = time.time()

now = datetime.datetime.now()



for y in [2017, 2018, 2019]:
    for m in range(1,13):
        for d in range(1,32):
            if m in [4,6,9,11] and d > 30:
                continue
            if m == 2 and d >28:
                continue
            # stop yesterday
            if y == 2019 and m > now.month:
                continue 
            if y == 2019 and m == now.month and d > now.day -1:
                continue
            url = "http://archive.luftdaten.info/%04d-%02d-%02d/%04d-%02d-%02d_sds011_sensor_299.csv"  %(y,m,d,y,m,d)
            outputFile = "data/sensor_299/%04d-%02d-%02d_sds011_sensor_299.csv"  %(y,m,d)
            print(url, outputFile)
            try:
                urllib.request.urlretrieve(url, outputFile)
            except:
                print("**** not available ****")
                continue

end = time.time()    
time = (end - start)
print("%f.2"  %(time))
