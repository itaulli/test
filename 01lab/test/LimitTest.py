"""
Created on Thu Jan 25 14:31:46 2018
Author: Ian Taulli
Discription: estimates the largest float, the smallest positive float, and the machine epsilon
"""
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

#%% Finds the largest float64 number

try:
    
    for i in range(400):
    
        n = 10.0**i
        
        if np.isinf(n) == True:
            break
        
except:
    pass
    
n = 0

try:
    
    for j in np.arange(i-1,i,0.01):
        
        n = 10.0**j
    
        if np.isinf(n) == True:
            break
        
except:
    pass

n = 0

try:
    
    for k in np.arange(j-0.01,j,0.0001):
        
        n = 10.0**k
        
        if np.isinf(n) == True:
            break
        
except:
    pass

n = 10.0**(k-0.0001)

print("max float estimate:",n)

#%% Finds the smallest float64 number

try:
    
    for l in range(400):
    
        n = 10.0**(-l)
        
        if n == 0.0:
            break
        
except:
    pass

n = 0.0

try:
    
    for m in np.arange(l-1,l,0.01):
    
        n = 10.0**(-m)
        
        if n == 0.0:
            break
        
except:
    pass

try:
    
    for p in np.arange(m-0.01,m,0.0001):
    
        n = 10.0**(-p)
        
        if n == 0.0:
            break
        
except:
    pass

n = 10.0**(-(p-0.0001))

print("min float estimate:",n)

#%% Finds the machine precision

i, j = 0, 0

for i in np.arange(1,20,0.1):
    
    j = 10.0**(-i)
    
    if 1.0 == 1.0 + j:
        break

for var in np.arange(i-1,i,0.0001):
    
    j = 10.0**(-var)
    
    if 1.0 == 1.0 + j:
        break

n = 10**(-(var-0.0001))

print("machine precision estimate:",n)

















