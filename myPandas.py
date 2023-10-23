import pandas as pd

data = {'name': ['john','nelly','cylia'],
        'age':[45,32,17],
        'profession':['actor','doctor','student']
        }

csv_path="fichier.csv"
df = pd.DataFrame(data) #create a dataframe
df.to_csv(csv_path)
print(df.head())    #By default, it displays the first 5 rows of the DataFrame

#df = pd.read_csv(csv_path) #from csv file to dataframe