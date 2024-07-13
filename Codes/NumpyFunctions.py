import numpy as np

a = np.array([78, 32, 63, 44, 8])
b = np.array([12, 26, 51, 88, 92])

n = len(a)
m = len(b)

print(a)
print(b)

from numpy import *

lns = linspace(10, 30, 6)
print(lns)

lgs = logspace(0, 10, 5)
print(lgs)

arg = arange(8, 22, 4)
print(arg)

z = zeros(3, int)
print(z)

o = ones(6, float)
print(o)

print(min(a + 2)) #adds 2 to minimum element of the array

cmp = where(a > b, a, b)
print(cmp)

for i in range(n):
    print(a[i] > b[i], end = ' ')    
print("\n",cmp, sep = '')

print(any(cmp))
print(all(cmp))

print("Original Array :")
ar = arange(5,11)
print(ar)

print("\nCopied Array :")
arcp = ar
print(arcp)

print("\nId of Original Array :")
print(id(ar))

print("\nId of Copied Array :")
print(id(arcp))

arcp[2] = 20

print("\nNew Original Array :")
print(ar)
print(id(ar))

print("\nNew Copied Array :")
print(arcp)
print(id(arcp))

print("\nViewing Original Array :")
arv = ar.view()
print(arv)
print(id(arv))

print("\nCopying Original Array :")
arc = ar.copy()
print(arc)
print(id(arc))

print("\nId of Original Array :")
print(id(ar))

ar[4] = 77

print("\nViewing Original Array :")
arv = ar.view()
print(arv)
print(id(arv))

print("\nCopying Original Array :")
arc = ar.copy()
print(arc)
print(id(arc))

print(ar)
print(id(ar))
print("\n")

print(a,"\n")

s=a[2:5:2]
print(s)

s=a[-2:2:-1]
print(s)

s=a[:-2:]
print(s)

a1d = array([10, 12, 14, 16, 18, 20])
print(a1d)

a2d = array([[2,4,6],[4,8,12]])
print(a2d)

a1r1 = reshape(a1d, (2,3))
print(a1r1)

a1r2 = reshape(a1d, (3,2))
print(a1r2)
print(a1r2[1:2,1:4])

a2r = reshape(a2d, (3, 2))
print(a2r)

rnd = random.rand(15)
print(reshape(rnd,(3,5)))

a3d = [[[1, 3, 5],[2, 4, 6]],[[7, 9, 11],[8, 10, 12]]]
for i in range(len(a3d)):
    for j in range(len(a3d[i])):
        for k in range(len(a3d[i][j])):
            print(a3d[i][j][k],  end = ' ')
