import numpy as np

#Creating Array

arr1d = np.array([1,2,3,4,5,6])
arr2d = np.array([[1,2,3],[4,5,6]])
x = [1,2,3,4,5,6]
y = [[1,2,3],[4,5,6]]

print(arr1d, x)
print(arr2d, y)

#Accessing Array
print(arr1d[1:4])
print(arr2d[0])

#Math Operators
arr_math1 = np.array([1,2,3])
arr_math2 = np.array([4,5,6])
print(arr_math1 + arr_math2, x+y)

#Reshape

arr_r = np.array([1,2,3,4,5,6])
print("Reshape: ", arr_r.reshape(2,3))

#Statistics operators

arr_stat = np.array([1,2,3,4,5,6])
print("Mean: ", np.mean(arr_stat))
print("Max: ", np.max(arr_stat))
print("Sum: ", np.sum(arr_stat))



