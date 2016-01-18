import numpy as np
import Data
import learners
import parameters

import cProfile

# import parameters
# import sys
# import matplotlib.pyplot as plt
# import Datapoint
# import entropy_gains

# import world
# import time
# import random



def main(A=1, N=1, R=2):

	model=learners.MixedLearner(theta=0.2)
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


def load_data():
	data=Data.Data(parameters.inputfile_kids)
	data.read(astext=False)
	return data


def misprediction_count(model, data, subject, max_action=None):

	if max_action is None:
		max_action=data.get_kid_nactions(subject)

	mispredictions=np.zeros(max_action)
	subject_sequence=data.data[subject][:max_action]

	for i in range(max_action):
		model_actions=model.choose_action(subject_sequence[:i-1])
		if subject_sequence[-1].get_action() != model_actions:
			mispredictions[i]=1

	return np.mean(mispredictions)




# def main(player, n, n_subs=None):

# 	if n_subs is not None:
# 		n_kids=n_subs
# 	else:
# 		n_kids=parameters.n_kids
	
# 	starttime=time.clock()

# 	data=Data.Data(parameters.inputfile_kids)
# 	#data=Data.Data(parameters.inputfile_adults)
# 	data.read(astext=False)

# 	truncate=int(n)
# 	n_r_random=parameters.n_r_random

# 	eg=np.zeros(len(data.get_kids()[:n_kids]))	

# 	n_long_kids=sum([data.get_kid_nactions(kid)>=truncate \
# 					 for kid in data.get_kids()])

# 	eig=np.zeros((n_long_kids,3))
	
# 	subactions=[]
# 	tlactions=[]
# 	mlactions=[]
# 	pgactions=[]
# 	rlactions=[]

# 	k=0
# 	for ki,kid in enumerate(data.get_kids()[:n_kids]):
# 		print 'Run for {0} actions, processing kid {1} out of {2}'.format(truncate, ki+1, n_kids)
# 		if data.get_kid_nactions(kid)<truncate:
# 			continue
		
# 		#get kid's action sequence
# 		kidseq=data.data[kid][:truncate]
# 		keg=entropy_gains.theory_expected_final_entropy(kidseq[-1].action,kidseq[:-1])
		
# 		#print 'kid {0} entropies: {1}'.format(k,kents)
		
# 		#compute optimal choice entropy gain with kid's action sequence
# 		tl=learners.TheoryLearner()
# 		tlaction=tl.choose_action(kidseq[:truncate-1])
# 		tlactions.append(tlaction)
# 		yokedseq=kidseq[:-1]+[Datapoint.Datapoint(tlaction, False)]#this False is generic, shouldn't be taken into account
# 		tleg=entropy_gains.theory_expected_final_entropy(tlaction, kidseq[:-1])
		
# 		#print tlents

# 		reg=0
# 		rlactions.append([])
# 		for r in range(n_r_random):
# 			rl=learners.RandomLearner()
# 			rlaction=rl.choose_action(kidseq[:truncate-1])
# 			rlactions[k].append(rlaction)
# 			yokedseqr=kidseq[:-1]+[Datapoint.Datapoint(rlaction, False)]#this False is generic, shouldn't be taken into account
# 			reg+=entropy_gains.theory_expected_final_entropy(rlaction, kidseq[:-1])
			
# 		reg/=n_r_random
		

# 		eig[k,0]=tleg
# 		eig[k,1]=reg
# 		eig[k,2]=keg

# 		#print "Action {0}, Subject {1}:\n Subject {2}\n Theory


# 		#print 'k: {0}, r:{1}, t:{2}'.format(keg, reg, tleg)
# 		k+=1



	
# 	# if player in ['theoryfull', 'jointfull', 'hypfull']:
# 	# 	filename=parameters.output_directory+player+'-'+str(truncate)+'_tru-'\
# 	# 			+str(n_r_random)+'_rreal.txt'
# 	# 	np.savetxt(filename, eig)

# 	# 	with open(parameters.output_directory+player+'-modelactions-'+str(truncate)+'_tru-'+\
# 	# 		str(n_r_random)+'_rreal.txt','w') as f:
# 	# 		for kact in tlactions:
# 	# 			f.write(str(kact)+'\n')

# 	# 	with open(parameters.output_directory+player+'-randomactions-'+str(truncate)+'_tru-'+\
# 	# 		str(n_r_random)+'_rreal.txt','w') as f:
# 	# 		for kact in rlactions:
# 	# 			f.write(str(kact)+'\n')


# 	print 'time elapsed for run {0}: {1:.0f} s'.format(filename, time.clock()-starttime)





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

