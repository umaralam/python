#!/usr/bin/python3

#point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
print(point)

point["x"] = 10
point["z"] = 30
print(point)
if "a" in point:
	print(point["a"])
print(point.get("a", 0))
del point["x"]
print(point)

for key in point:
	print(key, point[key])
for x in point.items():
	print(x)
for key, value in point.items():
	print(key, value)

