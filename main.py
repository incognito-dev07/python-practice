import math

radius = float(input("Enter the radius (cm): "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * pow(radius,2)

print("\nResults:")

print(f"The diameter is: {diameter}")
print(f"The circumference is: {round(circumference,2)} cm")
print(f"The area is: {round(area,2)} cm")
