
import ActiveLearner
import entropy_gains

class TheoryLearner(ActiveLearner):
	"""docstring for TheoryLearner"""
	def __init__(self):
		super(TheoryLearner, self).__init__()
		#self.model = Model.Model()
	
	def entropy_gain(self, action, data=None):
		return entropy_gains.theory_entropy_gain(action, data)
	


	# def entropy_gain(self, action, data=None):
	# 	expval=0
	# 	for d in world.possible_data(action):
	# 		alldata=[d] if data is None else [d]+data
	# 		expval+=utils.H(lambda t: model.p_theory_data(t, alldata), model.t_space)*\
	# 				model.p_data_action(d,action,data)
	# 	return expval


