#!/usr/bin/python3
from timeit import timeit

code1 = """
def calculate_xfactor(age):
	if age <= 0:
		raise ValueError("Age can not be 0 or less.")
	return 10 / age

try:
	calculate_xfactor(-1)
except ValueError as error:
	print(error)
"""
code2 = """
def calculate_xfactor(age):
        if age <= 0:
                return None
        return 10 / age

try:
        calculate_xfactor(-1)
except ValueError as error:
	pass

"""
print("first code", timeit(code1, number=10000))
print("second code", timeit(code2, number=10000))

