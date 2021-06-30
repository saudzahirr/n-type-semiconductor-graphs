import matplotlib.pyplot as plt 
import numpy as np

q = 1.6E-19
ni = 1.90189E10
up = 480
un = 1350
ND = [1E15, 2E15, 3E15, 4E15, 5E15]
values=[]
for x in ND:
    p = (x + ni)/(q*((un*x*x) + (un*ni*x) + (up*ni*ni)))
    values.append(p)
plt.plot(ND, values, label = "Curve") 
plt.xlabel('Concentration of the Donor atoms.')  
plt.ylabel('Resistivity of Silicon.') 
plt.legend() 
plt.savefig("Restivity_Concentration.png")
plt.show()
