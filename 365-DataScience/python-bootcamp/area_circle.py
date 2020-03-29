
# Problem: Ask a user for the radius of a circle and then print the area! 
# A = pi(r^2)
radius = int(input('Please type a value for the radius: '))
pi = 3.14

area = pi*(radius**2)
print("The radius is: " + str(radius) + "The area of the circle is: " + str(area))