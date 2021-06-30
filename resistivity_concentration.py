import matplotlib.pyplot as plt 
import numpy as np

q = 1.6E-19                                                    #charge of electron.
ni = 1.90189E10                                                #concentration of intrinsic silicon at room temperature. [carrier/cubic cm]
up = 480                                                       #holes mobility.    [square cm/V.s]
un = 1350                                                      #electron mobility. [square cm/V.s]
ND = [1E15, 2E15, 3E15, 4E15, 5E15]                            #donor atom concentration (Phosphorus). [carrier/cubic cm]
values=[]
for x in ND:
    p = (x + ni)/(q*((un*x*x) + (un*ni*x) + (up*ni*ni)))       #'p' is resistivity of doped semiconductor. [ohm.cm]
    values.append(p)
plt.plot(ND, values, label = "Curve") 
plt.xlabel('Concentration of the Donor atoms.')  
plt.ylabel('Resistivity of Silicon.') 
plt.legend() 
plt.savefig("Restivity_Concentration.png")
plt.show()
