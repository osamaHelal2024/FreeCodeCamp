import numpy as np 
import pandas as pd 
import seaborn as sns 
from matplotlib import pyplot as plt 

data = pd.read_csv("Epa_Level_Sea.csv")
data.head()
data['CSIRO Adjusted Sea Level'].value_counts(dropna= False)
data['CSIRO Adjusted Sea Level'].fillna(data['CSIRO Adjusted Sea Level'].mean() , inplace = True) 
data['CSIRO Adjusted Sea Level'].value_counts(dropna= False)
data['Lower Error Bound'].unique()
data['Lower Error Bound'].value_counts(dropna= False)
data['Lower Error Bound'].fillna(data['Lower Error Bound'].mean() , inplace= True)
data['Lower Error Bound']
data['NOAA Adjusted Sea Level'].unique()
data['NOAA Adjusted Sea Level'].value_counts(dropna= False)
data['NOAA Adjusted Sea Level'].fillna(data['NOAA Adjusted Sea Level'].median() , inplace = True) 
data['NOAA Adjusted Sea Level'].unique()
data['Upper Error Bound'].fillna(data['Upper Error Bound'].mean() , inplace= True)
data['Upper Error Bound'].unique()
# stage 2 
plt.scatter(data['Year'] , data['CSIRO Adjusted Sea Level'])
plt.title(" CSIRO Adjusted Sea Level in  Years ")
plt.xlabel("Year") 
plt.ylabel("CSIRO Adjusted Sea Level")
plt.legend()
from scipy import stats 
from scipy import interpolate 
m = stats.linregress(data['Year'] ,  data['CSIRO Adjusted Sea Level'] )

m.slope
m.intercept
CSIRO_Adjusted_Sea_Level = np.array(data['CSIRO Adjusted Sea Level'])
x = data['Year']
plt.plot(data['Year'] , data['CSIRO Adjusted Sea Level'] , 'o' , label = "original data")
plt.plot(x, m.intercept + m.slope*x, 'r', label='fitted line')
plt.title(" CSIRO Adjusted Sea Level in  Years ")
plt.xlabel("Year") 
plt.ylabel("CSIRO Adjusted Sea Level")
plt.legend()
def regerssion(input) : 
     plt.plot(data['Year'],data['CSIRO Adjusted Sea Level'], 'o') 
     plt.plot(input , m.intercept + m.slope * input , 'r' , label = "Fitted line ")
     plt.title(" CSIRO Adjusted Sea Level in  Years ")
plt.xlabel("Year") 
plt.ylabel("CSIRO Adjusted Sea Level")
plt.legend() 
      
      

    
x = np.arange(1880 , 2061 , 1 )
x
regerssion(x)
val_2050 = m.intercept + m.slope * 2050
val_2050