
myList = [1, 2,3,4,5]
length = len(myList)
a=10
for indx in range(length):
    myList[indx]=a*myList[indx]
print(myList)


import numpy as np

mymatrix=np.mat(myList)
print(a*mymatrix)