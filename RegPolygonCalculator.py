import math
#prompting the user to enter the number of sides of the regular polygon
sidesNum = int(input("Enter the number of sides of the regular polygon: "))
sideLength = float(input("Enter the length of one of the sides: "))

#calculating the apothem
apothem = sideLength / (2 * math.tan(math.radians(180 / sidesNum)))

#calculating the perimeter
perimeter = sidesNum * sideLength

#calculating the area
area = 0.5 * (perimeter * apothem)

#calculating each interior angle
interAngle = (sidesNum - 2) * 180 / sidesNum

#printing the results:
print("Number of sides:", sidesNum)
print("Length of each side:", sideLength)
print("Perimeter", perimeter)
print("Apothem:", (f"{apothem:.4f}"))
print("Area:", (f"{area:.4f}"))
print("Interior angle:", interAngle)