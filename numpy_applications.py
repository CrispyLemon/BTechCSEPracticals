#create a program to manipulate numpy arrays
import numpy as np 
list1,list2=[x for x in range (0,10)],[x for x in range(10,20)]
arr = np.array([list1,list2])
print(arr)


print("1",arr[0],arr[1],sep="\n")
print('2',arr[0][3])
print('3',arr[0][2:6],arr[1][5:-1:-1],sep="\n")
print('4',arr[0:1][0:6:2])


print(arr.reshape(4,5))