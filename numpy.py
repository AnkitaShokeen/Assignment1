#Q1.Create a numpy array with 10 elements of the shape(10,1) using np.random and find out the mean of the elements using basic numpy functions.

import numpy as np
np_arr=np.random.rand(10,1)
print(np_arr)
print("Mean: ",np.mean(np_arr))


#Q2.Create a numpy array with 20 elements of the shape(20,1) using np.random find the variance and standard deviation of the elements. 

import numpy as np

np_arr=np.random.rand(20,1)
print(np_arr)

print("variance: ",np.var(np_arr))
print("standard deviation: ",np.std(np_arr))


#Q3.Create a numpy array A of shape(10,20) and B of shape (20,25) using np.random. Print the matrix which is the matrix multiplication of A and B. The shape of the new matrix should be (10,25). Using basic numpy math functions only find the sum of all the elements of the new matrix.

import numpy as np
a=np.random.rand(10,20)
b=np.random.rand(20,25)
c=np.dot(a,b)
print("matrix A",c)
print("matrix B ",c.shape)
print("Sum is: ",np.sum(c))


#Q4.Create a numpy array A of shape(10,1).Using the basic operations of the numpy array generate an array of shape(10,1) such that each element is the following function applied on each element of A.
#f(x)=1 / (1 + exp(-x)) 
#Apply this function to each element of A and print the new array holding the value the function returns
'''
Example:
a=[a1,a2,a3]   
n(new array to be printed )=[ f(a1), f(a2), f(a3)]
'''

import numpy as np

A=np.random.rand(10,1)
a=lambda x:(1/(1+np.exp(-x)))
print("New array:",np.array(list(map(a,A))))
