#!/usr/bin/python3

##Point Class##
class Point:
##class level attributes visible/accessed across all the instance of a Point class##
	default_color = "red"
##Constructor##
	def __init__(self, x, y):
		self.x = x
		self.y = y
##Function##
	def draw(self):
		print(f"Point ({self.x}, {self.y})")

##Changing class level attribute dynamically is visible across all the instance of the Point class##
Point.default_color = "Yellow"

##Point Class Object##
point = Point(1, 2)
##Call to the Point class draw function##
point.draw()
##instance accessing Point class attribute default_color##
##using instance reference or class reference. Both example shown below##
print(Point.default_color)
print(point.default_color)


##Another instance of a Point class##
another = Point(3, 4)
##Call to the Point class draw function##
another.draw()
##instance accessing point class attribute default_color##
##using instance reference##
print(another.default_color)
	
