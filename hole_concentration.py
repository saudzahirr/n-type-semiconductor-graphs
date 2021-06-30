import matplotlib.pyplot as plt 
import numpy as np

ni = 1.90189E10                                       #concentration of intrinsic silicon at room temperature. [carrier/cubic cm]
ND = [0, 1E10, 2E10, 3E10, 4E10, 5E10]                #concentration of donor atom (Phosphorus). [carrier/cubic cm]
values = []
for x in ND:
    np = (ni*ni)/(x + ni)                             #concentration of holes in n-type doping. [carrier/cubic cm]
    values.append(np)
plt.plot(ND, values, label = "Curve")  
plt.xlabel('Concentration of the Donor atoms.')  
plt.ylabel('Concentration of Holes.')  
plt.legend() 
plt.savefig("Holes_Concentration.png")
plt.show()
