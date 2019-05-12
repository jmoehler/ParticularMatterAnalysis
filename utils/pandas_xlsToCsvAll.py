import pandas as pd
data_xls = pd.read_excel('/Users/jakob/Dokumente/Schule/Jahresarbeit/Projekte/Feinstaub/data/Stuttgart/Halbstd-Werte-Stuttgart-Mitte-SZ_1987-2018.xlsx', 
    sheet_name=None, index_col=None)
all_data = pd.concat(data_xls.values(), sort=False)
all_data.to_csv('/Users/jakob/Dokumente/Schule/Jahresarbeit/Projekte/Feinstaub/data/Stuttgart/Halbstd-Werte-Stuttgart-Mitte-SZ_1987-2018.csv', encoding='utf-8')