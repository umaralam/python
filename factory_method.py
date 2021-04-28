#!/usr/bin/python3

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
##Point class method or factory method##
	@classmethod
	def zero(cls):
		return cls(0, 0)

	def draw(self):
		print(f"Point ({self.x}, {self.y})")

##Call to factory method/Point class method creates an object of Point class ("point" here)itself which can be used as a default object referencing:- Point (0, 0)##
point = Point.zero()
point.draw()
