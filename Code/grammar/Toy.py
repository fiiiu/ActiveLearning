
import WorldElement

class Toy(WorldElement):

	def __init__(self, color, shape):
		super(Toy, self).__init__(color, shape)

	def display(self):
		"Toy of color {0} and shape {1}".format(color, shape)