import numpy as np
import Data
import learners
import parameters
import AnalyzedData
import cProfile
import cPickle as pkl

# import parameters
# import sys
# import matplotlib.pyplot as plt
# import Datapoint
# import entropy_gains

# import world
# import time
# import random



def main(A=10, N=31, R=50):
	mps=np.zeros((11,2))
	for i,theta in enumerate(np.linspace(0,1,11)):
		mps[i][0]=theta
		mps[i][1]=run_global_theta(theta, A, N, R)

	with open('misprediction.pkl', 'wb') as f:
		pkl.dump(mps, f)
	
	print mps

def run_global_theta(theta, A, N, R):
	model=learners.TabulatedMixedLearner(theta, 'td_10A.pkl')
	data=load_data()
	subjects=data.get_kids()[:N]

	total_misp=0
	for subject in subjects:
		subject_misp=0
		for r in range(R):
			subject_misp+=misprediction_count(model, data, subject, max_action=A)

		print "Misprediction average, subject {0}, {1} realizations: {2}"\
					.format(subject, R, subject_misp/R)

		total_misp+=subject_misp/R

	print "Total misprediction average, {0} realizations: {1}"\
					.format(R, total_misp/N)

	return total_misp/N		


def load_data():
	data=Data.Data(parameters.inputfile_kids)
	data.read(astext=False)
	return data


def misprediction_count(model, data, subject, max_action=None):

	if max_action is None:
		max_action=data.get_kid_nactions(subject)
	else:
		max_action=min(data.get_kid_nactions(subject),max_action)

	mispredictions=np.zeros(max_action)
	subject_sequence=data.data[subject][:max_action]
	for i in range(max_action):
		model_actions=model.choose_actions(subject, i, subject_sequence[:i-1])
		#model_actions=adata[subject][i]['TMA']#model.choose_action(subject_sequence[:i-1])
		#print model_actions
		if subject_sequence[-1].get_action() not in model_actions:
			mispredictions[i]=1

	return np.mean(mispredictions)




if __name__ == '__main__':
# 	n=6
# 	if len(sys.argv)==1:
# 		player='kids'		
# 	else:
# 		player=sys.argv[1]
# 		if len(sys.argv)>2:
# 			n=int(sys.argv[2])
# 			if len(sys.argv)>3:
# 				parallel=bool(sys.argv[3])
	cProfile.run('main()')
 	#main()

