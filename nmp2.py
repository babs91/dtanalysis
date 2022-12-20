import numpy as np

print(np.ones([4,4]))

b=(np.full((2,3), 105))

a=(np.full((3,2), 100))


c = np.matmul(a,b)

print(c)


a = np.array([[1,2,3,4,5],[4,5,6,7,8],[1,0,0,0,0]])
print(a.shape)
print(a)


print(a[0,2])

v1=[1,2,4,6,8]
v2=[0,3,6,10,12]
v3=[10,12,14,15,16]

print(np.vstack([v1,v2,v3]))


v1[0] = 5
print(v1)
print(np.vstack([v1,v2,v3]))

print(np.random.randint(7,size=[3,3]))

print(np.random.rand(3,5))

print((np.identity(3)*5))


a_1 = np.ones([2,3])

a_2 = np.zeros([2,4])

print(np.hstack([a_1,a_2]))



