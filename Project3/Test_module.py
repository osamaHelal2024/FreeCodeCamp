import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt 
import seaborn as sns 

data = pd.read_csv("medical_examination.csv") 

data.head() 
# figrue 1 
# overwight column 
data.head()
data['height'] = data['height'] /100 
data.head()
data['overweight'] = data['weight'] /(data['height'] * data['height']) 
List  = data['overweight']
Listoverweight = []  
print(List) 

for x in List:
    if(x >25): 
        Listoverweight.append(1) 
    else:
        Listoverweight.append(0)
data['overweight'] = Listoverweight
data.head()
data['overweight'].unique()
data['gluc'].unique()
data['cholesterol'].unique()

data['cholesterol'].unique()
data['cholesterol'].replace(1, 0 , inplace= True) # if you swap this line you will make run time error 
data['cholesterol'].replace([2,3] ,1 , inplace = True) 

data['cholesterol'].unique()
data['gluc'].replace(1, 0 , inplace= True) # if you swap this line you will make run time error 
data['gluc'].replace([2,3] ,1 , inplace = True) 
data['gluc'].unique()
data
meltdata = data.iloc[ : , 7: -1  ]
meltdata= meltdata.join(data['overweight'])
meltdata.head()
df_cat = pd.melt(meltdata, var_name = 'variable', value_vars = ['active','alco','cholesterol', 'gluc','overweight','smoke'], id_vars = 'cardio') # and this too 
df_cat
fig = sns.catplot(data=df_cat, kind="count",  x="variable",hue="value", col="cardio").set_axis_labels("variable", "total")
fig = fig.fig # look for it too 
fig.savefig('catplot.png')

df_heat = data[(data['ap_lo']<=data['ap_hi']) &
(data['height'] >= data['height'].quantile(0.025))&
(data['height'] <= data['height'].quantile(0.975))&
(data['weight'] >= data['weight'].quantile(0.025))&
(data['weight'] <= data['weight'].quantile(0.975))
    ]

df_heat
corr = df_heat.corr()
    

    # Generate a mask for the upper triangle
   
mask = np.triu(corr)  # look for it i mean 
    
fig, ax = plt.subplots(figsize=(7, 5))
    

    # Draw the heatmap with 'sns.heatmap()'
sns.heatmap(corr,mask=mask, fmt='.1f',vmax=.3, linewidths=.5,square=True, cbar_kws = {'shrink':0.5},annot=True, center=0)
  

    # Do not modify the next two lines
fig.savefig('heatmap.png')