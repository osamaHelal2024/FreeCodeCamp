from Test_module import Test_module 

RUN  =  Test_module() 
#run.calculate([0,1,2,3,4,5,6,7,8]) 

# import everything from tkinter module
from tkinter import *   
root = Tk()             
 
# Open window having dimension 100x100
root.geometry('400x400')

btn  = Button(root , text="run" , bd='5' , command=lambda:RUN.calculate())   
btn.pack(side='top')
 
root.mainloop()

 
