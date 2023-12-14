import pandas_datareader as pdr

# Spécifiez le symbole de l'action que vous souhaitez récupérer
symbol = 'AAPL'  # Par exemple, pour Apple

# Obtenez les données à l'aide de pandas_datareader depuis Yahoo Finance
data = pdr.get_data_yahoo(symbol, start='2023-01-01', end='2023-12-31')  # Spécifiez la plage de dates souhaitée

# Affiche les premières lignes des données récupérées
print(data.head())
