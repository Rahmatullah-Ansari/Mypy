import numpy as np
print(np.array([1,2,3,4,5,6]))
print(np.__version__)
#slicing
arr=np.array([1,2,3,4,5,6])
print(arr[2:5:2])
#datatype
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )
print(arr.dtype)
#creating array with defined datatype.
ar=np.array([1.1,2.2,3.3,4.4],dtype='f')
print(ar.dtype)
#datatype conversion.
nr=ar.astype('i')
print(nr.dtype)
#copy array
na=nr.copy()
na[0]=12
print(na)
#view 
m=na.view()
m[1]=15
print(m)
print(na)
#check array has it's own data or not
x=m.copy()
y=m.view()
print(x.base)
print(y.base)
#shape of array-number of element in each dimention.
my=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(my.shape)
#creating array with a specified dimention.
myar=np.array([1,2,3,4,5],ndmin=8)
print(myar.shape)
#reshape
a=np.array([1,2,3,4,5,1,3,5])
print(a)
aa=a.reshape(2,2,2)
print(aa)
#iterating over 3d array.
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)
#array join
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)
#split an array.
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)
#array search.
arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)
#array sort.
arr = np.array([3, 2, 0, 1])

print(np.sort(arr))
#array filter.
arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)