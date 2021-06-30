import matplotlib.pyplot as plt 

ND = [0,1E10,2E10,3E10,4E10,5E10] 
final_ND=[]
ni = 1.90189E10
for each in ND:
    s=each+ni
    final_ND.append(s)
nn=final_ND
plt.xlabel('Concentration of the Donor atoms.')  
plt.ylabel('Concentration of Electrons.') 
plt.plot(ND, nn, label = "Curve")   
plt.savefig("Electron_Concentration.png")
plt.legend() 
plt.show() 
