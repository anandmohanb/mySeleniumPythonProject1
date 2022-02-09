from numpy import *

arr = array([5,4,7,3,2])
for i in range(len(arr)):
    for j in range(i,len(arr)-1):
        k=i
        if arr[k] > arr[j+1]:
            k = 0
            k = j + 1
            temp = arr[i]
            arr[i] = arr[k]
            arr[k] = temp

print("Ascending order : ", arr)