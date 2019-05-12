import pandas as pd
import time

start = time.time()
4
years = range(1999,2019,1)

for y in years:
    print(y)
    df = pd.read_excel('./data/Stuttgart/Halbstd-Werte-Stuttgart-Mitte-SZ_1987-2018.xlsx', 
        sheet_name= str(y), index_col=None)
   

    df.to_csv('./data/StuttgartCsv/Halbstd-Werte-Stuttgart-Mitte-SZ_%s.csv' %(y), 
       encoding='utf-8')
    
end = time.time()

time = end-start

print("Sec: %.4f" %(time))