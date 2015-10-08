
import ActiveLearner
import random
import world


class RandomLearner(ActiveLearner):
	"""docstring for RandomLearner"""
	def __init__(self):
		super(RandomLearner, self).__init__()
		#self.model = Model.Model()
		
	def choose_action(self, prev_data=None):
		return random.choice(world.possible_actions)
		