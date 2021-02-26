import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = [1, 2, 3, 4, 5]

print(a)
print(b)

a = a + 1
# b = b + 1 #error
b = b + [1]

print(a)
print(b)

c = np.arange(1, 10, 2)
print(c)
# linspace (a,b,c) dari a sampe b dengan jarak sama berelemen c
d = np.linspace(0, 10, 3)
print(d)
e = np.array([(1, 2, 3), (3, 2, 1)])
print(e)
z = np.zeros((2, 10))
print(z)

# Matriks Identitas
print("identity")
h1 = np.identity(3)
print(h1)
h2 = np.eye(5)
print(h2)

# operasi matriks
a1 = [1, 2, 3, 4]
b1 = [2, 4, 4, 7]

a2 = np.array([1, 2, 3, 4])
b2 = np.array([2, 4, 4, 7])
res1 = a1+a1
res2 = a2 + b2
print(res1)
print(res2)
