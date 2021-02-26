import torch

x= torch.empty(3)
print(x)

y=torch.empty(2,2,3,3)
print(y)

a=torch.zeros(2,1,3)
print(a)

b=torch.tensor([2.5,0.1])
print(b)

c= torch.rand(2,2)
d= torch.rand(2,2)
print ("c dan d")
print (c)
print(d)
z=c*d
print("tes")
z1 = torch.mul(c,d)
print (z)
print(z1)