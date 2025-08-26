import pandas as pd 

estoqueHub = pd.read_csv("estoque_HUB.csv", sep=',', engine='python')
estoqueTray = pd.read_csv("estoque_TRAY.csv", sep=',', engine='python')

merged = pd.merge(estoqueHub, estoqueTray, on='sku', how='inner', suffixes=('_hub', '_tray'))
print(merged.head(15))