#coding:utf-8
import string
import matplotlib.pyplot as plt  
import numpy as np
import math

x=9
base=3
N=30
B=np.zeros(N)
E=np.zeros(N)
F=np.zeros(N)
r=x

for i in range(0,N):
	print(i)
	E[i]=2**(-i)
	B[i]=base**E[i]
print(E)	
print(B)	

for i in range(0,N):
	if B[i]<=r:
		F[i]=1
		r=r/B[i]
	else: 
		F[i]=0
print(F)
y=np.dot(E,F)
print("log",base," ",x,"=",y)

