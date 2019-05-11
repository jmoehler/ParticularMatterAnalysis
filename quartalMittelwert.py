import pathlib
import csv
import time
import datetime




# die angaben
year    = 2018               #year          
sensor  =  299               #sensor
quartal =    2             #quartal


# die Monate eines Quartals 
qMonths = []

# Start der Zeit für die Zeitmessung
start = time.time()

# das aktuelle Datum
now = datetime.datetime.now()


# definierung des Quartals
if quartal == 4:
    months = [10,11,12]
    qMonths.extend(months)

elif quartal == 3:
    months = (7,8,9)
    qMonths.extend(months)

elif quartal == 2:
    months = (4,5,6)
    qMonths.extend(months)

elif quartal == 1:
    months = (1,2,3)
    qMonths.extend(months)
else:
    print("invalid quartal")

sPM2_5 = []
sPM10 = []

# Anzahl der PM2_5 und PM10 Werte
anzAll = 0

# Summe aller addierten PM10 Werte
wertAllPM10 = 0

# Summe aller addierten PM2_5 Werte
wertAllPM2_5 = 0

# das herraussuchen der files in einem Quartal
for y in [year]:
    for m in qMonths:
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

            path = "data/sensor_%d/%04d-%02d-%02d_sds011_sensor_%d.csv"  %(sensor,y,m,d,sensor)
            



            try:
                with open(path,newline = '') as f:
                    readers = csv.DictReader(f, delimiter= ';')
                    for row in readers:
                        PM10 = float(row["P1"])
                        PM2_5 = float(row["P2"])
                        sPM10.append(PM10)
                        sPM2_5.append(PM2_5)
                        pass
                print(path)
            except:
                print("file %04d-%02d-%02d is not avalible" %(y,m,d))
                
                

            for i in range(0, len(sPM10)):
                    
                #PM10 
                wertAllPM10 += sPM10[i]
                anzAll += 1



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

print("Der Feinstaubwert (PM10) lag im %d. Quartal des Jahres %d bei %.2f μm pro m^3" 
%(quartal,year, durchWertPM10))
print("Der Feinstaubwert (PM2_5) lag im %d. Quartal des Jahres %d bei %.2f μm pro m^3" 
%(quartal,year, durchWertPM2_5))

print("Sec: %.4f" %(diff)) 