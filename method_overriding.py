#!/usr/bin/python3
##Extending or modifying the method defined in the base class i.e. method_overriding. In this example is the call to constructor method##
class Animal:
	def __init__(self):
		print("Animal Constructor")
		self.age = 1

class Mammal(Animal):
	def __init__(self):
		print("Mammal Constructor")
		self.weight = 2
		super().__init__()

	def eat(self):
		print("eats")

m = Mammal()
print(m.age)
print(m.weight)
