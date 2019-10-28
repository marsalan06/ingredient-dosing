import csv

import pandas as pd
recipe_name=str(input("Enter Product: "))
print("Getting recipe for "+recipe_name+" ....")
tonnage=str(input("Enter Tonnage: "))
print("Aquiring wrt to tonnage: "+str(tonnage)+" tons")
combo=recipe_name+".csv"
data=pd.read_csv(combo)
data.set_index('chemical',inplace=True)
data.head()
print(data)
index_no=int(len(data.index))
print("Total contents of recipe "+str(index_no)+".")
for i in range(0,index_no):
    print(data.index[i]+": "+str(data[tonnage].iloc[i])+" gms")  #column name in first, row name in second
