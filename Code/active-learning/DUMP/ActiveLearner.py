
import utils
import model
import world

class ActiveLearner(object):
	"""docstring for ActiveLearner"""
	def __init__(self):
		pass
		
	def choose_action(self, prev_data=None):
		mingain=1000
		astars=[]
		for a in world.possible_actions():
			this_gain=self.entropy_gain(a, prev_data)
			#print a, this_gain
			if this_gain <= mingain:
				astars.append(a)
				mingain=this_gain
		return random.choice(astars)


