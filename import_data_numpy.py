import numpy as np

filename= "test.csv"
data = np.loadtxt(filename,delimiter=',',skiprows=1,dtype=str)


data_2rwos = np.loadtxt(filename,delimiter=',',skiprows=1,usecols=[0,2],dtype=str)
print(data)

