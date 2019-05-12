import csv
import time

from datetime import datetime

start = time.time()
i=0
o=0

header = []
# resultfile
year = range(1987,2019,1)
for y in year:
    with open('./data/StuttgartCsvDone/Halbstd-Werte-Stuttgart-Mitte-SZ_%d_D.csv' %(y),
        'w', newline='') as csvfile:
        writer_csv = csv.writer(csvfile, delimiter=';')
        # lesefile
        for datafile in ['./data/StuttgartCsv/Halbstd-Werte-Stuttgart-Mitte-SZ_%d.csv' %(y)]:
            with open(datafile,newline = '') as f:
                readers = csv.reader(f, delimiter= ',')
                for row in readers:
                    i += 1
                    
                    # 1. Spalte entfernen
                    row.pop(0)
                    # wenn mehr als 5 Spalten dann weiter
                    if (len(row) < 5):
                        continue

                    # Datum in Spalte 1 (row[0])
                    dateStr = row[0]

                    # Zeit in Spalte 2 (row [1])
                    timeStr = row[1]

                    # die Kopfzeilen zusammenfassen
                    if dateStr == "Datum":
                        for s in range(0, len(row)):
                            header.append(row[s] + "-" + prevRow[s])
                        
                        writer_csv.writerow(header)


                        continue
                    
                    
                    try:
                        # das Datum anpassen
                        date1 = datetime.strptime(dateStr, '%Y-%m-%d 00:00:00') 
                        row[0] = date1.strftime('%Y-%m-%d') 
                        
                        # die Zeit anpassen
                        hTime = datetime.strptime(timeStr, '%H:%M:%S')
                        row[1] = hTime.strftime('%H:%M')
                        
                    except: 
                        try:
                            # falls zeit so geschrieben ebenfalls anpassen
                            datetime.strptime(dateStr, '%m/%d/%y')
                            row[0] = date.strftime('%Y-%m-%d') 
                      
    
                        except: 
                            # alste zeile speichern ( um sie eventuell mit anderer Zeile zu verbinden)
                            prevRow = row
                            continue

                print(y)
                    
            f.close()


ende = time.time()
diff = ende-start

print ("wrote %d (of %d) rows" % (o,i))
print("runtime: %.5fs" %(diff))