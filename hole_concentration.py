import matplotlib.pyplot as plt 
import numpy as np

ni = 1.90189E10
ND = [0, 1E10, 2E10, 3E10, 4E10, 5E10] 
values=[]
for x in ND:
    np = (ni*ni)/(x+ni)
    values.append(np)
plt.plot(ND, values, label = "Curve")  
plt.xlabel('Concentration of the Donor atoms.')  
plt.ylabel('Concentration of Holes.')  
plt.legend() 
plt.savefig("Holes_Concentration.png")
plt.show() 
