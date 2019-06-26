"""
encode as for machine to understand(numerical)
ordinal
nominal
"""

import pandas as pd

ordered_satisfaction=['very unhappy','unhappy','neutral','happy','very happy']
df=pd.DataFrame({'satisfaction':['mad','happy','unhappy','neutral']})		#catagorical value
print(df)

df['satisfaction2']=df.satisfaction.astype(dtype='category', ordered=True, categories=ordered_satisfaction)
print(df)		#new column satisfaction2 with as type

print(df.dtypes)

df.satisfaction2=df.satisfaction2.cat.codes		#gives index of the satisfaction2 in satisfactiion
print(df.satisfaction2)

df=pd.DataFrame({'vertebrates':['bird','mammal','fish','amphibian','reptile','bird','mammal']})
print(df)

df['vertebrates2']=df.vertebrates.astype("category").cat.codes
print(df)

#get_dummies()- essential boolean variables
df=pd.get_dummies(df, columns=['vertebrates'])
print(df)