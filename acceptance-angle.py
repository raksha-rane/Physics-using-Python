#theta-imax : also known as waveguide acceptance angle
import math
n1 = float(input("Enter refractive index of core of optical fiber: "))
n2 = float(input("Enter refractive index of cladding of optical fiber: "))
acc = math.asin(math.sqrt((n1**2)-(n2**2)))
print("The acceptance angle of the optical fiber is", acc)
