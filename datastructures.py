#to find the area of the circle
import math
radius= float (input(" Input the radius of the circle:"))
area = math.pi* (radius**2)
print("The area of the circle with radius", end = " "); print(radius, end= " "); print ("is:", end= " "); print( area)



#to print the extension of filename
x = input("Input the Filename:")
s = x. split('.')
s = s[1]
t= "py"
if ( s==t):
    print(" The extension of the file is:", end = " "); print("python")
else:
    print(" ")
    
