#Calculation of Average value of electric field
#intiation of all variables 
#Given that
import math

p = float(input("Enter power in watt: ")  # power in watt
d = float(input("Enter distance from light source: ")   # Distance from lamp in m
epsilon_0 = 8.854e-12     # Permittivity of free space
mu_0 = 4*math.pi*1e-7     # Permeability of free space
s = p/(4*math.pi*d**2)    # Calculation of pointing vector
E_H_ratio = math.sqrt(mu_0/epsilon_0)    # Calculation of ratio of Electric field and magnetic field
E= math.sqrt(E_H_ratio*s)                # Calculation of  Electric field 
print("Average value of electric field at distance", d, "in Volt/m:"),round(E,2)
