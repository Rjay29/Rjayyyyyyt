import math

r = float(input("Enter diameter: "))
diam = r / 2
surface_area = 4 * math.pi * (diam ** 2)
print(f"Diameter of the sphere: {r :.0f1}")
print(f"Surface area of sphere is:  {surface_area :.4f}" )
volume = ((4/3) * math.pi) * (diam ** 3)
print(f"Volume of sphere is:  {volume:.4f}")
