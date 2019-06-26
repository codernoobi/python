"""
series- one type data
dataframe- collection of series stacked horizontally
rows- axis=1
column- axis=0
"""
import pandas as pd
import numpy as np
s=pd.Series([1,3,2,np.nan,6,8])         #when using series dont save any file as pandas.py, it throws an error
print(s)

"""
df=pd.read_excel('my_dataset.xlsx', 'sheet1', na_values=['NA','?'])
df=pd.read_json('my_dataset.json', orient='columns')

dfs=d.read_html('http://www.textfixer.com/tutorials/css-tables.php')		#looks for tables in the page and loads to dataframe object
#create list
len(dfs)			#gives the number of tables
df=dfs[0]			#use the index from len to get perticular df

#all behaves diff

#pandas allow to directly access sql db
from sqlalchemy import create_engine
engine= create_engine('sqlite:///:memory:')
df=pd.read_sql_table('my_table',engine, columns=['ColA','ColB'])
"""

df=pd.read_csv("eg.csv",sep=',')

#sep, delimeter, header, names, index_col, skipinitialspace, skiprows, na_values, thousands, decimal
df.head(10)		#prints the first 10 results
df.tail(10)		#prints the last 10 result
df.describe()		#shows all numerical columns
df.index()		#shows the range
df.dtypes		#info of datatypes of all columns

