#!/usr/bin/python3

from collections import namedtuple

##Code 1 represents data class as it does not have behavior/function, just the data.##
Code1 = """
class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)
"""

##Below program is exactly the same as above achieved using namedtuple class##
##namedtuple assigned to a class Point##
Point = namedtuple("point", ["x", "y"])

p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
##comparing 2 objects for equality without implementing mgic method "__eq__(self, other)"##
print(p1 == p2)
