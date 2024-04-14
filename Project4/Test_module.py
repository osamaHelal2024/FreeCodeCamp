import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

from  matplotlib.pyplot import figure  
class Test_module():
    def calculate(self):
        plt.style.use("seaborn")
        data  = pd.read_csv("FreeCodeCamp.csv") 
        datagroupby = data
        data.head()
        data['date'] = pd.to_datetime(data['date'] , format = '%Y-%m-%d' )
        data['Year'] = data['date'].dt.year
        data['Month']  =data['date'].dt.month
        data['day'] =data['date'].dt.day
        data['NameMonth'] = data['Month'].replace(np.arange(1,13).tolist() , ['January', 'February', 'March', 'April', 'May', 'June', 'July',  'August', 'September', 'October', 'November', 'December']  ) 
        data 
        data = data[
            (data["value"] >= data["value"].quantile(0.025))
            & (data["value"] <= data["value"].quantile(0.975))
        ]
        len(data)
        datagroupby = data 
        plt.plot(data['date'] , data['value']) 
        plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019') 
        plt.xlabel("Date") 
        plt.ylabel("PageViews") 

        gk = datagroupby.groupby('Month')
        gk.first()
        gk
        def Draw_bar_plot():
            g= sns.catplot( kind = 'bar' , x = 'Year' , y = "value" , data = data , hue = "NameMonth"  , hue_order= ['January', 'February', 'March', 'April', 'May', 'June', 'July',  'August', 'September', 'October', 'November', 'December'] ,legend_out = False )
            g.set(title = "Average Page Views.", xlabel  = "Year" , ylabel = " Average Page Views." )    
            plt.title('Months')
        Draw_bar_plot()
        def Draw_box_plot_Year():
            sns.boxplot(x = 'Year', y = 'value', data =data, palette = 'tab10').set(
            title = 'Year-wise Box Plot (Trend)',  xlabel='Year',  ylabel='Page Views') 

        Draw_box_plot_Year()
        def Draw_box_plot_Month():
            sns.boxplot(x = 'value', y = 'NameMonth', data =data, palette = 'tab10').set(
            title = 'Month-wise Box Plot (Seasonality)',  xlabel='Average Page Views.',  ylabel='Months') 
        Draw_box_plot_Month()
