

import WorldElement

class Box(WorldElement):

	def __init__(self, color, shape):
		super(Box, self).__init__(color, shape)

	def display(self):
		"Box of color {0} and shape {1}".format(color, shape)