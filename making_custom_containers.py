#!/usr/bin/python3

##A container is a data structure i.e. list,set,dictionary and so on. A custom container is nothing but the customized piece of code using one of the built-in
## data structure/container which works smartly for example a dictonary returns value of each key case sensatively so a custom container can be created to return 
##the value of each key case insensatively using dictionary built-in data structure as shown below##

class TagCloud:
##cunstructor to initialize tags as an empty dictonary##
	def __init__(self):
		self.tags = {}

	def add(self, tag):
		self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

	def __getitem__(self, tag):
		return self.tags.get(tag.lower(), 0)

	def __setitem__(self, tag, count):
		self.tags[tag.lower()] = count

	def __len__(self):
		return len(self.tags)
	
	def __iter__(self):
		return iter(self.tags)

cloud = TagCloud()

cloud.add("java")
cloud.add("Python")
cloud.add("python")
cloud.add("python")
cloud["c++"] = 10

print(f"number of tags: {len(cloud)}")

for tag in cloud:
        print(tag)

python = cloud["python"]
java = cloud["java"]
cplus = cloud["c++"]

print(f"python: {python}")
print(f"java: {java}")
print(f"c++: {cplus}")
