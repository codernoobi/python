import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

matplotlib.style.use('ggplot')

#histogram

df=pd.read_csv('3eg.csv')		#import data
print(df.columns)		#look at data


#histograms are one of the 7 basic tools of quality graphical techniques
#most helpful in troubleshooting issues

df.asymmetry.plot.hist(title='Asymmetry',bins=6)
plt.show()		#creating histogram plotting asymmetry feature
df.asymmetry.plot.hist(title='Asymmetry',bins=10)
plt.show()

#plotting multiple graphs together
df[df.wheat_type=='rosa'].asymmetry.plot.hist(alpha=0.4)		#plot based  on wheat type
df[df.wheat_type=='kama'].asymmetry.plot.hist(alpha=0.4)		#alpha adjusts transperency
df[df.wheat_type=='canadian'].asymmetry.plot.hist(alpha=0.4)
plt.show()

"""
# If the above line throws an error, use plt.style.use('ggplot') instead
student_dataset = pd.read_csv("students.data", index_col=0)
my_series = student_dataset.G3
my_dataframe = student_dataset[['G3', 'G2', 'G1']] 
	
my_series.plot.hist(alpha=0.5)
my_dataframe.plot.hist(alpha=0.5)
"""

#scatter plot
