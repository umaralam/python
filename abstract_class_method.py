#!/usr/bin/python3
from abc import ABC, abstractmethod

##InvalidOperationError is Custome exception derived from Exception class##
class InvalidOperationError(Exception):
	pass

class Stream(ABC):
	def __init__(self):
		self.opened = False

	def open(self):
		if self.opened:
			raise InvalidOperationError("Stream is already opened.")
			self.opened = True

	def close(self):
		if not self.opened:
			raise InvalidOperationError("Stream is already closed.")
			self.opened = False

##Abstract method needs to be created in Stream class for common method read in derived classes##

	@abstractmethod
	def read(self):
		pass

class FileStream(Stream):
	def read(self):
		print("Reading stream from file")

class NetworkStream(Stream):
	def read(self):
		print("Reading stream from network")
##TypeError: Can't instantiate abstract class Stream with abstract methods read##
#stream = Stream()

##FileStream and Network stream classes are inherited from Stream class.
##open and close function of Stream class should not be visible or Stream() should not be allowed to create. Stream class shoild be Abstract##

#stream.open()

fileStream = FileStream()
networkStream = NetworkStream()

print(fileStream.read())
print(networkStream.read())
