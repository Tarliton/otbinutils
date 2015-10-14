import os

class File():
	def __init__(self, version, extension):
		self.file = open("things/"+str(version)+"/Tibia"+"."+extension, "r")

	def __del__(self):
		self.file.close()

