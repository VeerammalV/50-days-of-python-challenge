#To find the area of the triangle
#Three sides of the triangles a, b, c are provided by the user.

First = float(input('Enter the first: '))
Second= float(input('Enter the second: '))
Third = float(input('Enter the third: '))

#calculating the semi-parameter
s = (First+Second+Third)/2

#calculating the area

Area = (s*(s-First)*(s-Second)*(s-Third)**0.5)
print("The area of the triangle is ",Area)