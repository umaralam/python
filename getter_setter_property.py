#!/usr/bin/python3

class Product:
	def __init__(self, price):
##No data validation in place##
#		self.price = price

##Letting setter to set the price so that the validation is performed on the input##
#		self.set_price(price)

##Since using decorator for property object our constructor will get modified as##
		self.price = price		

##price getter##
#	def get_price(self):
#		return self.__price

##price setter

#	def set_price(self, value):
#		if value < 0:
#			raise ValueError("Price can not be negative.")
#		self.__price = value

##setting property for getter and setter of product price##
#	price = property(get_price, set_price)

##With the above property implementation get_price and set_price is still directly accessible from outside. To avoid that we need to define
##property in a better way using decorator object rather than making getter and setter private using "__"##

	@property
	def price(self):
		return self.__price

	@price.setter
	def price(self, value):
		if value < 0:
                        raise ValueError("Price can not be negative.")
		self.__price = value
	

##Passed negative value. Python accepts it without validation##

product = Product(10)
##Directly accessing the price field to get the product price##

#print(product.price)

##getting price by calling getter since price field is no longer accessible directly##

#print(product.get_price())

##Instead of calling getter and setter we can call the property object to get and set the price like a regular field access##

#product.price = -1
print(product.price)
