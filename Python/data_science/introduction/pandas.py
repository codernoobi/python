#10 minutes to pandas pandas.org
"""
numpy - one type data
pandas - multiple type data

row correspond to observation
column correspond to variable
"""
import pandas as pd
pandascsv=pd.read_csv("eg.csv", index_col=0)		#the row indexes are also seen as column 
print(pandascsv)                                    #to resolve this specify index of first column which contain row index

print(eg["Contact"])		#to select specific column
"""
brics.country

brics["on_earth"]=[true,true,true,true,true]		#adding new column

brics["density"]=brics["population"]/brics["area"] * 1000000		#new column from existing columns

brics.loc["BR"]		#gives row data based on row label arg

brics.loc["ch","capital"]		#access both row and column
brics["capital"].loc["ch"]
brics.loc["ch"]["capital"]
"""
