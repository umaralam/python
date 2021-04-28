#!/usr/bin/python3
try:
	age = int(input("Age: "))
	xfactor = 10 / age
except (ValueError, ZeroDivisionError):
	print("Enter the valid age.")
else:
	print("Execution Continues")
