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
                    

                    row.pop(0)

                    if (len(row) < 5):
                        continue

                    dateStr = row[0]
                    timeStr = row[1]

                    
                    if dateStr == "Datum":
                        for s in range(0, len(row)):
                            header.append(row[s] + "-" + prevRow[s])
                        
                        writer_csv.writerow(header)


                        continue
                    
                    
                    try:
                        date1 = datetime.strptime(dateStr, '%Y-%m-%d 00:00:00') 
                        row[0] = date1.strftime('%Y-%m-%d') 
                        
                        hTime = datetime.strptime(timeStr, '%H:%M:%S')
                        row[1] = hTime.strftime('%H:%M')
                        
                    except: 
                        try:
                            datetime.strptime(dateStr, '%m/%d/%y')
                            row[0] = date.strftime('%Y-%m-%d') 
                      
    
                        except: 
                            prevRow = row
                            continue

                print(y)
                    
            f.close()


ende = time.time()
diff = ende-start

print ("wrote %d (of %d) rows" % (o,i))
print("runtime: %.5fs" %(diff))