import numpy as np

#Create sample list
mylist1=[1,2,3,4]
mylist2=[5,6,7,8]

#Create array from sample list
myarray1=np.array(mylist1)
print(myarray1)

#Create multidimensional (2D) array
myarray2=np.array([mylist1,mylist2])
print(myarray2)

#Find dimension of array
print(myarray2.shape)

#Finding the datatype of array elements
print(myarray2.dtype)

#Working with special functions in numpy
#1. zeros: Creates a new numpy array of dimension (x,y). If only 1 value is mentioned as parameter x, then dimension of array is (1,x)
print(np.zeros(4))

#2. ones: Creates a new numpy array of dimension (x,y). If only 1 value is mentioned as parameter x, then dimension of array is (1,x)
print(np.ones(5))

#3. empty: Similar to zeros function. We get output as numpy array with random values close to zero
print(np.empty(3))

#4. eye: Creates an identity matrix of order n. Order is a parameter for the function
print(np.eye(3))

#5. arange: It is an arithmetic progression function taking 3 parameters (start, stop, diff).
# start is the 1st term; stop is final term (not included in the final AP array); diff is the diff between consecutive terms of AP
print(np.arange(1,5,2))

#------- NEXT LECTURE -------#

#Scalar operations on arrays

#Python 2.x assumes '/' as integer division  as default. To use floating-point division, use 'from __future__ import division'
#Python 3.x uses '/' as floating point division and '//' as integer division

#Array multiplication
print(myarray1*myarray1) #This gives element wise multiplication and the array is considered as scalar

#Exponential multiplication
print(myarray1**3)

#Subtraction in array is scalar in nature
print(myarray2-myarray2)

#Reciprocal operation on arrays gives reciprocal of each element
print(1/myarray1)

#-------- NEXT LECTURE -------#

#Indexing Numpy Arrays (1D Arrays)
arr = np.arange(0,12)
print(arr) #Print whole array
print(arr[0]) #Print element at 0th index of array
print(arr[0:5]) #Print array elements from index 0 to index 4 (both inclusive)

arr[0:5]=20 #Sets the values of arr from index 0 to 4 (both inclusive) to 20
print(arr)

#IMPORTANT POINT
arr2=arr[0:6] #Store sliced array part of arr from index 0 to index 5 (both inclusive) in arr2
arr2[:]=29 #Assign all elements of arr2 as 29
print(arr2)
print(arr) #Here the indices of arr from 0 to 5 (both inclusive are also modified the same way as arr2, since arr2 is just a sliced part of
#           arr itself, and all the changes in arr2 will be reflected in arr. Numpy seeks to reduce the memory utilisation, hence data is not
#           copied, but shared between the arrays. Every operation on arr and arr2 is performed onto the same memory location

#To create a copy of the same array in numpy using copy() function
arr_copy=arr.copy() #arr_copy and arr point to different memory locations

#-------- NEXT LECTURE --------#

#Indexing Numpy Arrays (Multidimensional Arrays)

arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)

#Slices of 2D array
slice1=arr2d[0:1,0:2] #This slice stores row index 0(1st row) and column indices 0,1(1st 2 columns)
#print(slice1)

slice2=arr2d[:2,1:]
#print(slice2)
#Other 1D indexing operations and setting values are allowed for multidimensional arrays as well

for i in range(len(arr2d)):
    arr2d[i]=i
#print(arr2d) #If we use single index to access the elements of a rD array, then the index is considered as the row index and
#             refers to all the elements of that row

#print(arr2d[[0,1]]) #Another method of accessing array rows using row numbers

#--------- NEXT LECTURE --------#

#Other important array functions

#1. arange()
A=np.arange(1,15,2)
print(A)

#2. sqrt(array)
B=np.sqrt(A)
print(B)

#3. exp(array)-returns array whose elements are e raised to the corresponding element of input array
C=np.exp(A)
print(C)

#4. add(array1,array2)-returns the summation of corresponding elements of the 2 arrays.
#   Overall, the returned value is an array of the same dimension as array1 and array2
print(np.add(A,B))

#5. maximum(array1,array2)-compares corresponding elements of array1 and array2 and returns the maximum out of the two.
#   Overall, the returned value is an array of the same dimension as array1 and array2
print(np.maximum(A,B))

#Reference Links for Numpy: www.scipy.org

#---------- NEXT LECTURE ----------#

#Saving and loading arrays from external memory(For situations where the variable is too large to be stored without external memory)

#Saving single arrays
arr=np.arange(10)
#print(arr)
np.save('saved_arr.npy',arr) #A new file called saved_arr is created with the Numpy format and this stores the array arr
new_array=np.load('saved_arr.npy') #load is used to load an existing Numpy file
print(new_array)

#Saving Multiple arrays
#Multiple arrays are stored as a zip file or archive file
array1=np.arange(25)
array2=np.arange(30)
np.savez('saved_arrays.npz',x=array1,y=array2)
new_arrayz=np.load('saved_arrays.npz')
print(new_arrayz['x'])

#Saving to a .txt file
np.savetxt('textfile_array.txt',array1,delimiter=',')
text_load=np.loadtxt('textfile_array.txt',delimiter=',')
print(text_load)
