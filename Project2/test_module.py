class test_module:
        def calculate(self):
            import numpy as np 
            import pandas as pd 
            data = pd.read_csv("adult.csv") 
            data[data['workclass'].duplicated()]
            Label = ['White', 'Black', 'Asian-Pac-Islander', 'Other',
                'Amer-Indian-Eskimo']

            List = [len(data[data['race'] == "White"]) ,  
            len(data[data['race'] == "Black"])  , 
            len(data[data['race'] == "Asian-Pac-Islander"]) ,  
            len(data[data['race'] == "Other"])   , 
            len(data[data['race'] == "Amer-Indian-Eskimo"] ) ] 

            # First Stage
            pd.Series(List, index = Label)
            # Second stage 
            mean = data['age'].mean()
            # Thrid Stage 
            print(len(data[data['education'] == 'Bachelors']) / len(data['education']) *100)  
            print(len(data[data['education'] == 'Masters']) / len(data['education']) *100)  
            print(len(data[data['education'] == 'Doctorate']) / len(data['education']) *100)  




            data['income'].unique()
            data['hours.per.week'].min()
            data[data['hours.per.week'].min() and data['income'] == '>50K']
            data['hours.per.week'].unique()
            data['native.country'].unique()
            data['native.country'].value_counts()
            data['native.country'].replace('?' ,'United-States' , inplace = True )
            data['native.country'].unique()
            data['occupation'].unique()
            data['occupation'].replace('?' , 'India' , inplace = True) 
            data['occupation'].value_counts()
            data[data['occupation'] == 'India' &  data['income'] == '>50K']
            data['education.num'].unique()
            data.head()
            data['workclass'].value_counts()
            data['workclass'].replace('?' , 'Never-worked' , inplace= True)
            data['workclass'].unique()
            data['income'].unique() 