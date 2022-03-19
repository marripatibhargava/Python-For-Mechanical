d1 = int(input("Inner Diameter: "))
d2 =  int(input("Outer Diameter: "))
P = int(input("Load: "))
L = int(input(" Length of the Cylinder: "))
E = float(input("Modulus of Electricity: "))

#Calculation
A = (3.14/4)*((d2**2)-(d1**2)) #Area(mm^2)
S = P/A #Stress

print("Stress in the cylindrical rod ", round(S), "Mpa")

deflection = ((P*L)/(A*E))
e = deflection/L   #Strain

print("Stan in the post is %e", e)