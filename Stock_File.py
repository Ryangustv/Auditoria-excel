import pandas as pd 
#import openpyxl --case you prefer import archive xlxs 

stockA = pd.read_csv("estoque_TRAY.csv", sep=',', engine='python')
stockB = pd.read_csv("estoque_HUB.csv", sep=',', engine='python')

stock_merged = pd.merge(stockB, stockA, on='sku', how='inner', suffixes=('_A', '_B'))
stock_merged['difference'] = stock_merged['estoque_A'] - stock_merged['estoque_B']

#stock_merged.to_excel('StockWithDifference.xlsx', index=False)
stock_merged.to_csv('StockWithDifference.csv', index=False)

print("Archive 'StockWithDifference.csv' as been genetared! xD")
