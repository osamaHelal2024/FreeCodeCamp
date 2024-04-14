Listargument = [] 
import pandas as pd 
import numpy as np 
  
class test_module(): 
    def calculate(self, ListParameter):
        if(ListParameter.index(ListParameter[-1]) !=8):
            print("List must contain nine numbers")
            exit()
        else:
            npListFloat  = np.array( ListParameter , dtype = float)
            npListint = np.array( ListParameter, dtype= int ) 
            npListFloatshape = npListFloat.reshape(3,3)
            npListintshape = npListint.reshape(3,3)  
        # no we will make the operaiton on the numpy array and convert it to list 
                #First mean operaiton 
            List_Mean_axis1 = npListFloatshape.mean(axis  = 0 ).tolist()
            List_Mean_axis2 = npListFloatshape.mean(axis = 1 ).tolist() 
            List_Mean_Flatten = npListFloatshape.mean().tolist() 
                #Second Varaince operation 
            List_Variance_axis1 = npListFloatshape.var(axis=0).tolist()
            List_Variance_axis2 = npListFloatshape.var(axis = 1 ).tolist() 
            List_Variance_Flatten = npListFloatshape.var().tolist()
                # Thrid Max operation  
            List_Max_axis1 = npListintshape.max(axis=0).tolist()
            List_Max_axis2 = npListintshape.max(axis = 1 ).tolist() 
            List_Max_Flatten = npListintshape.max().tolist()
                # Fourth standrad deviation operation 
            List_Std_axis1 = npListFloatshape.std(axis=0).tolist()
            List_Std_axis2 = npListFloatshape.std(axis = 1 ).tolist() 
            List_Std_Flatten = npListFloatshape.std().tolist()
                    # Fifth min operation 
            List_Min_axis1 = npListintshape.min(axis=0).tolist()
            List_Min_axis2 = npListintshape.min(axis = 1 ).tolist() 
            List_Min_Flatten = npListintshape.min().tolist() 
                    #Sixth Sum Operation 
            List_Sum_axis1 = npListintshape.sum(axis = 0).tolist()
            List_Sum_axis2 = npListintshape.sum(axis = 1).tolist()
            List_Sum_Flatten = npListintshape.sum().tolist() 


            dictionary = {
    'mean': [List_Mean_axis1 , List_Mean_axis2 ,  List_Mean_Flatten ] , 
    'Variance': [List_Variance_axis1 , List_Variance_axis2 ,  List_Variance_Flatten ] ,  
    'standard deviation': [List_Std_axis1 ,List_Std_axis2 , List_Std_Flatten ] , 
    'Max' : [List_Max_axis1 , List_Max_axis2 , List_Max_Flatten] ,  
    'Min' : [List_Min_axis1 , List_Min_axis2 , List_Min_Flatten] ,  
    'Sum': [List_Sum_axis1 , List_Sum_axis2 , List_Sum_Flatten] 
    
}
            print(dictionary) 


    
         
