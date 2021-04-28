#!/usr/bin/python3
code1 = """
class Mammal:
	def eat(self):
		print("eat")

	def walk(self):
		print("walk")

class Fish:
	def eat(self):
		print("eat")

	def swim(self):
		print("swim")
"""
##In the above program eat method is repeated. Programmer should follow DRY.##

class Animal:
	def eat(self):
		print("eat")

##Inheritance in action##
class Mammal(Animal):
        def walk(self):
                print("walk")

##Inheritance in action##
class Fish(Animal):
        def swim(self):
                print("swim")

m = Mammal()
m.eat()
f = Fish()
f.eat()
