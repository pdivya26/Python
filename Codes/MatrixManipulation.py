import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[2, 4, 6],[8, 10, 12], [14, 16, 18]])

print("Matrix Addition : ") 
print(np.add(a, b))

print("\nMatrix Subtraction : ") 
print(np.subtract(b, a))

print("\nMatrix Multiplication : ") 
print(np.dot(a, b))

print ("\nElement-wise Matrix Multiplication : ") 
print (np.multiply(a,b))

print("\nMatrix Division : ") 
print(np.divide(b, a)) 

print("\nTranspose of Matrix - A : ")
ta = np.transpose(a)
print(ta)

print("\nTranspose of Matrix - B : ")
tb = np.transpose(b)
print(tb)

print ("\nTranspose of Matrix - A : ") 
print (a.T)

print ("\nTranspose of Matrix - B : ") 
print (b.T)

print ("\nSquare Root of Matrix - A : ") 
print (np.sqrt(a))

print ("\nSquare Root of Matrix - B : ") 
print (np.sqrt(b))
