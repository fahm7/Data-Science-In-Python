import numpy as np

height = [1.5, 2.5, 1.7, 1.3, 0.9,2.6]
weight= [60, 84, 68, 40, 28, 63 ]


np_height= np.array(height)
np_weight=np.array(weight)


print(np_height)
bmi = np_weight/np_height**2

print("_____________BMI____________")
print(bmi)

####################### List REMARKS ##################################

l1= [1.4, True , "fam" ]

np_l1= np.array(l1)

print(l1)
print (np_l1)

mylist= [1,2,3]

sum= mylist+mylist
print(sum)

npsum= np.array(mylist)+np.array(mylist)

print (npsum)

####################### SUB Setting ##################################

print(bmi[1])

print(bmi>24)

print( bmi[bmi>24])

##################### DIMENTIONS ####################################

print (type(np_height))
print (type(np_weight))

np_2d = np.array([[1.5, 2.5, 1.7, 1.3, 0.9,2.6] ,
                   [60, 84, 68, 40, 28, 63 ]] )

print(np_2d.shape)
print(np_2d[0])
print(np_2d[1][2])

print(np_2d[1,2])
print("_______ : __________ \n")
print(np_2d[:,2])
print(np_2d[:,1:3])

print(np_2d[1,:])


##################### Statistics ####################################
print("_"*50)
#Calculation the mean height of all family members
print(np_2d[0])
print(np.mean(np_2d[1]))
print(np.median(np_2d[1]))
print(np.sort(np_2d[1]))
print(np.std(np_2d[1]))
