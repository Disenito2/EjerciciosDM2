# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 15:56:21 2021

@author: 99gar
"""

Hola buenos dias

FrA=179.4 
FrB=947.5 
Yf=1.5
Qa= FrA/(2*Yf) 
Qb= FrB/(2*Yf)
Fa=185.6
e=0.4
Xr=0.4
Yr=1.5
C=120000
n=2600

if (Qb+Fa)>Qa:
    Qa= Qb+Fa
else:
    Qb= Qa-Fa
    
    
if (Qa/FrA)>e:
    Pa=Xr*FrA+Yr*Qa
else:
    Pa=FrA
    
if (Qb/FrB)>e:
    Pa=Xr*FrB+Yr*Qb
else:
    Pb=FrB
    
L10a=(C/(Pa*10))**(10/3)*((10**6)/(60*n))
L10b=(C/(Pb*10))**(10/3)*((10**6)/(60*n))
    
print ("L10a",L10a)
print("L10b",L10b)
print("Qa",Qa)
print("Qb",Qb)
print("Pa",Pa)
print("Pb",Pb)
