import pathlib
import csv
import time



y = 2017               #year
m = 5                  #month
d = 20                  #day
s = 299                #sensorName

path = "data/sensor_%d/%04d-%02d-%02d_sds011_sensor_%d.csv"  %(s,y,m,d,s)




print(path)

sPM2_5 = []
sPM10 = []


# Start der Zeit für die Zeitmessung
start = time.time()

with open(path,newline = '') as f:
    readers = csv.DictReader(f, delimiter= ';')
    for row in readers:
        PM10 = float(row["P1"])
        PM2_5 = float(row["P2"])
        sPM10.append(PM10)
        sPM2_5.append(PM2_5)
        pass
      

# Anzahl der PM2_5 und PM10 Werte
anzAll = 0

# Summe aller addierten PM10 Werte
wertAllPM10 = 0


for i in range(0, len(sPM10)):
        
    #PM10 
    wertAllPM10 += sPM10[i]
    anzAll += 1

# Summe aller addierten PM2_5 Werte
wertAllPM2_5 = 0

for i in range(0, len(sPM2_5)):
        
    #PM2_5
    wertAllPM2_5 += sPM2_5[i]

# Durchschnittswert = Summe aller Werte durch Anzahl aller Werte
durchWertPM10 = wertAllPM10 / anzAll
durchWertPM2_5 = wertAllPM2_5 / anzAll

# Ende der Zeit für die Zeitmessung
end = time.time()

# endzeit - Anfangszeit = benötigte Zeit
diff = end-start
 
print("Der Feinstaubwert (PM10) lag am %d.%d.%d bei %.2f µg/m³ " %(d,m,y,durchWertPM10))
print("Der Feinstaubwert (PM2_5) lag am %d.%d.%d bei %.2f µg/m³ " %(d,m,y,durchWertPM2_5))

print("Sec: %.4f" %(diff)) 