import numpy as np


def calculate(list):
  
    if len (list) != 9:
       raise ValueError("List must contain nine numbers.")
  
    list = np.array(list).reshape(3,3)
    
    
    mean =[list.mean(axis= 0).tolist(),list.mean(axis=1).tolist(),np.mean(list).tolist()]
    variance =[list.var(axis=0).tolist(),list.var(axis=1).tolist(),np.var(list).tolist()]
    std dev =[list.std(axis=0).tolist(),list.std(axis=1).tolist(),np.std(list).tolist()]
    max =[list.max(axis =0).tolist(),list.max(axis =1).tolist(),a.max()]
    min =[list.min(axis =0).tolist(),list.min(axis =1).tolist(),a.min()]
    sum =[list.sum(axis =0).tolist(),list.sum(axis =1).tolist(),a.sum()]
    
  
    return {

            "mean" : mean,
      
            "variance" : variance,
      
            "standard deviation" : std_dev,

            "max" : max,        

            "min" : min,

            "sum" : sum,



      
   }

