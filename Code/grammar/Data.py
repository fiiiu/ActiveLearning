
import Toy
import Box

class Data():

	def __init__(self):
		self.data=[]

	def add_datapoint(self, toy, box, result):
		self.data.append((toy, box, result))