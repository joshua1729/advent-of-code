import pandas as pd
import numpy as np
import os.path
import math


os.chdir('D:/Practise/advent_of_code/day_1')
df = pd.read_csv('input.csv',header=None)

#Solution of the first part
df.columns = ['module_weight']
df['fuel']=(np.floor(df['module_weight']/3))-2

print(df['fuel'].sum())


#Solution of the second part

#Function to calculate total fuel
def total_fuel(weight,tot_fuel,fuel):
    if ((math.floor(weight/3))-2)>=0:
        fuel=(math.floor(weight/3))-2
        weight=fuel
        return(fuel+total_fuel(weight,tot_fuel,fuel))
    else: 
        return(0)
    return(0)

#Code and invoking the function
df['total_fuel']=0

for i in range(0,100):
    df.iloc[i,2]=total_fuel(df.iloc[i,0],0,0)
    
print(df['total_fuel'].sum())
