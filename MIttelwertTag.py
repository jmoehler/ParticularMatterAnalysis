import pathlib
import csv
import time

start = time.time()

y = 2017                #year
m = 1                   #month
d = 20                  #day
s = 299                 #sensor

path = "data/sensor_%d/%04d-%02d-%02d_sds011_sensor_%d.csv"  %(s,y,m,d,s)




print(path)

sPM2_5 = []
sPM10 = []



with open(path,newline = '') as f:
    readers = csv.DictReader(f, delimiter= ';')
    for row in readers:
        PM10 = float(row["P1"])
        PM2_5 = float(row["P2"])
        sPM10.append(PM10)
        sPM2_5.append(PM2_5)
        pass
      

wertAllPM10 = 0
wiedAll = 0

for i in range(0, len(sPM10)):
        
    #PM10
    wertAllPM10 += sPM10[i]
    wiedAll += 1

wertAllPM2_5 = 0

for i in range(0, len(sPM2_5)):
        
    #PM2_5
    wertAllPM2_5 += sPM10[i]

 
durchWertPM10 = wertAllPM10 / wiedAll
durchWertPM2_5 = wertAllPM2_5 / wiedAll

print("Der Feinstaubwert (PM10) lag am 10.3.2017 bei %.2f μm pro m^3" %(durchWertPM10))
print("Der Feinstaubwert (PM2_5) lag am 10.3.2017 bei %.2f μm pro m^3" %(durchWertPM2_5))
end = time.time()
diff = end-start
print("Sec: %.4f" %(diff)) 


