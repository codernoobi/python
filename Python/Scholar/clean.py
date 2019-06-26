#cleaning data
"""
outliers
holes
...
"""
#for incomplete data

import numpy as np
import pandas as pd

df=pd.read_csv('eg.csv',sep='\t')		#read a data set
print(df)
print(df.dtypes)

#fixing dates
df.Date=pd.to_datetime(df.Date, errors='raise')		#raise an exception
print(df)								#errors='coerce'	set as nan/nat
print(df.dtypes)						#errors='ignore'	retuen the input

#fixing names
None==None		#true
np.nan==None		#false

df.lastname==np.nan
df.LastName.isnull()

df.FirstName.str.containers('')
selector=df.FirstName.str.contains('')& df.LastName.isnull()
print(selector)

#df.LastNmae[selector]=df.FirstName[selector].apply(lambda x: x.split(' '[1]))	#take first name split it add second half to last name
#df.FirstNmae[selector]=df.FirstName[selector].apply(lambda x: x.split(' '[0]))	#add first half to first name

df.loc[selector,'LastName']=df.FirstName[selector].apply(lambda x: x.split(' ')[1])
df.loc[selector,'FirstName']=df.FirstName[selector].apply(lambda x: x.split(' ')[0])
print(df)

import re
df.Height=df.Height.apply(lambda x : re.sub('[^0-9]','',str(x)))
df.Weight=df.Weight.apply(lambda x : re.sub('[^0-9]','',str(x)))

df.Height= pd.to_numeric(df.Height, errors='coerce')
df.Weight= pd.to_numeric(df.Weight, errors='coerce')

df.Age.unique()		#guves all unique values in a column
df.Age.value_counts()	#counts the repetation of all distinct values

#get rid of column which is not needed
df=df.drop(labels=['Height2','Weight2'],axis=1)

#remove duplicates based on certain columns(subset of features)
ddf.drop_duplicates(subset=['FirstName','LastName','Gender','Age'], inplace=True)
print(df)

#fill nan with scalar
df.fillna(0)

#do per feature
#calculate mean for feature and replace
df.fillna(df.mean(axis=0))
print(df.mean(axis=0))

#fill forward/backward with previous values
df.fillna(method='ffill',limit=1)	#method=bfill

#interpolate polynomial. check nan position
df.interpolate(method='polynomial',order=2)

#drop all rows with holes
df.dropna(axis=1)		#index will be incomplete
df.dropna(axis=0)		#drop columns with holes

df=df.dropna(axis=0, thresh=4)		# Drop any row with NaNs that has at least 4 non-NaNs within it
df = df.drop(labels=['Features', 'To', 'Delete'], axis=1)	#drop perticular columns

bad_rows=df[df.Date.isnull()].index
df.drop(bad_rows, inplace=True)

df.Gender.fillna('M', inplace=True)		#fill gender with male default
df.Occupation.fillna('.Unspecified', inplace=True)		#unspecified
print(df)

df.reset_index(inplace=True)		#reset index after droping rows
print(df)				#keeeps original index and creates new index

df.reset_index(drop=True,inplace=True)		#reset index after droping rows
print(df)					#does not retain the original index

#df = df.dropna(axis=0, thresh=2).drop(labels=['ColA', axis=1]).drop_duplicates(subset=['ColB', 'ColC']).reset_index()		#all drop queries in one statement