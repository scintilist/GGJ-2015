from collections import defaultdict

class PublicRecord(defaultdict):
	def __init__(self):
		defaultdict.__init__(self, self.__class__)
