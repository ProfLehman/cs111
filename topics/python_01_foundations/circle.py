# circle.py
# Author: Prof. Lehman
# Date: September 25, 2026
# Description: Calculate the circumference and area of a circle given radius


# Input
radius = float(input("Enter the radius of the circle: "))

# Processing
pi = 3.14
circumference = 2 * pi * radius
area = pi * radius ** 2

# Output
print()
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.2f}")