
import HypothesisFactory
import parameters
import model


#class Theory():

# def __init__(self, kind):
# 	self.kind=kind
# 	self.n_theories=parameters.n_theories
# 	self.machines=parameters.machines
# 	self.hf=HypothesisFactory.HypothesisFactory()

def unnormalized_posterior(data=None):
	if data is None:
		return prior()
	else:
		return data_likelihood(data)*prior()

def data_likelihood(data=None):
	lik=1
	for machine in self.machines:
		hyp_lik=0
		allhyp=self.hf.create_all_hypotheses(machine)
		for hyp in allhyp:
			hyp_lik+=hyp.likelihood(data)*self.hypothesis_likelihood(hyp)
		lik*=hyp_lik

	return lik


def prior():
	return 1.0/model.n_theories


def hypothesis_likelihood(theory_kind, hypothesis):
	
	if theory_kind==0:
		return int(hypothesis.kind==0)
	
	elif theory_kind==1:
		return int(hypothesis.kind==1)

	elif theory_kind==2: #color match
		if hypothesis.kind==2 and hypothesis.color==hypothesis.machine[0]:
			return 1
		else:
			return 0
	
	elif theory_kind==3: #shape match
		if hypothesis.kind==3 and hypothesis.shape==hypothesis.machine[1]:
			return 1
		else:
			return 0

	elif theory_kind==4: #color AND shape match
		if hypothesis.kind==4 and hypothesis.color==hypothesis.machine[0]\
			and hypothesis.shape==hypothesis.machine[1]:
			return 1
		else:
			return 0

	elif theory_kind==5: #color OR shape match
		if hypothesis.kind==5 and (hypothesis.color==hypothesis.machine[0]\
			and hypothesis.shape==hypothesis.machine[1]): #check this and. only 1 gets support.
			return 1
		else:
			return 0

	elif theory_kind==6: #specific color (ANY color)
		if hypothesis.kind==2: 
			return 1
		else:
			return 0

	elif theory_kind==7: #specific shape (ANY shape)
		if hypothesis.kind==3:
			return 1
		else:
			return 0

	elif theory_kind==8: #specific shape AND color (ANY)
		if hypothesis.kind==4:
			return 1
		else:
			return 0

	elif theory_kind==9: #NOT match color
		if hypothesis.kind==2 and hypothesis.color!=hypothesis.machine[0]:
			return 1./(parameters.n_colors-1)
		else:
			return 0
	
	elif theory_kind==10: #NOT match shape
		if hypothesis.kind==3 and hypothesis.shape!=hypothesis.machine[1]:
			return 1./(parameters.n_shapes-1)
		else:
			return 0

	elif theory_kind==11: #INDEPENDENT
		return 1./self.hf.n_hypotheses(hypothesis.machine)

	#CHECK CHECK CHECK THIS SALADDD




