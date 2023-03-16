# Calculating V-number : also known as normalized frequency
# it is equal to area of core divided by wavelength of light times numerical aperture
import math
d = float(input("Enter diameter of the core of optical fiber: "))
v = float(input("Enter wavelength of light entering the optical fiber: "))
na = float(input("Enter numerical aperture: "))
v_n = ((math.pi*d)/v)*na
print("The V-number is:", v_n)
