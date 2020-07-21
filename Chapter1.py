import numpy as np

v = np.sqrt( (2*46.1*10**3*1.602e-19)/(4*1.66510e-27) )

print("v:",v)

m1 = 4*1.6605e-27
m2 = 4*1.6605e-27
m = 8*1.6605e-27

a = 0.5*m
b = -1*np.sqrt(3)*m2*v
c = 2*m2*v**2 - 0.5*m*v**2 - 92.2e3*1.60218e-19
v1 = np.roots([a,b,c])

print([a,b,c])
print("v1",v1)
