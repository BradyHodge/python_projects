# Made by Brady Hodge
# CSE 110
# 04 Teach: Team Activity - Speed of a Falling Object

import math

m = float(input("mass (in kg) "))
g = float(input("acceleration due to gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter) "))
t = float(input("time (in seconds) "))
p = float(input("density of fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water) "))
A = float(input("cross sectional area of projectile (in square meters) "))
C = float(input("drag constant (0.5 for sphere, 1.1 for cylinder falling on it's side. You could look it up for other shapes.) "))

c = (1/2) * p * A * C
v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))

print(f"The inner value of c is: {c:.3f}")
print(f"The velocity after {t} seconds is: {v:.3f}m/s")