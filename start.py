
import csv
import time
from datetime import datetime

start = time.time()
end = time.time()
diff = end-start

with open('data/sensor_299/2017-02-01_sds011_sensor_299.csv' ,newline = '') as f:
    readers = csv.DictReader(f, delimiter= ';')
    for row in readers:
        PM10 = float(row["P1"])
        PM2_5 = float(row["P2"])
       # time = datetime.strptime(timeStr, '%Y-%m-%dT%H:%M:%S.%f+00:00')  
        print("PM10 = %.2f,  PM2,5 = %.2f" %(PM10,PM2_5))
      


