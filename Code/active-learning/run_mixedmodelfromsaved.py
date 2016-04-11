import numpy as np
import Data
import learners
import parameters
import AnalyzedData
import cProfile
import cPickle as pkl
import matplotlib.pyplot as plt
import seaborn as sns


def main_global(group, filename, A=10, N=31, R=50):
	nsteps=25
	mps=np.zeros((nsteps,2))
	for i,theta in enumerate(np.linspace(0,1,nsteps)):
		mps[i][0]=theta
		mps[i][1]=run_global_theta(group, filename, theta, A, N, R)

	#with open('misprediction.pkl', 'wb') as f:
	#	pkl.dump(mps, f)
	
	plot(mps)
	print mps

def main_individual(group, filename, A=10, N=31, R=50):
	nsteps=25
	data=load_data(group)
	subjects=data.get_kids()[:N]
	results=np.zeros((N,3))
	print('yeye')
	for i, subject in enumerate(subjects):
		run=run_individual_theta(filename, subject, data, A, R, nsteps)
		results[i,:]=run
		# print mintheta, misp, err 
		# results[i,0]=mintheta
		# results[i,1]=misp

	print results
	plot_individual(results)

def plot_individual(results):
	plt.hist(results[:,0])
	plt.xlabel('theta')
	plt.xlim([0,1])
	plt.show()
	plt.hist(results[:,1])
	plt.xlabel('Average Misprediction')
	plt.show()
	plt.errorbar(results[:,0],results[:,1],yerr=results[:,2],fmt='o')
	plt.xlabel('theta')
	plt.xlim([0,1])
	plt.ylabel('Average Misprediction')
	plt.show()


def plot(mps):
	plt.plot(mps[:,0], mps[:,1])
	#WRONG plt.errorbar(mps[:,0], mps[:,1], yerr=(0.1, 0.1), marker='o')
	plt.xlabel('theta')
	plt.ylabel('ave misprediction')
	plt.show()

def run_global_theta(group, filename, theta, A, N, R):
	model=learners.TabulatedMixedLearner(theta, filename)
	data=load_data(group)
	subjects=data.get_kids()[:N]

	total_misp=0
	for subject in subjects:
		subject_misp=0
		for r in range(R):
			subject_misp+=misprediction_count(model, data, subject, max_action=A)

		#print "Misprediction average, subject {0}, {1} realizations: {2}"\
		#			.format(subject, R, subject_misp/R)

		total_misp+=subject_misp/R

	print "Total misprediction average, {0} realizations: {1}"\
					.format(R, total_misp/N)

	return total_misp/N	


def run_individual_theta(filename, subject, data, A, R, nsteps):	
	misp=np.zeros((nsteps,3))
	for i,theta in enumerate(np.linspace(0,1,nsteps)):
		theta_misp=0
		model=learners.TabulatedMixedLearner(theta, filename)

		theta_misps=[misprediction_count(model,data,subject,max_action=A) for r in range(R)]
		#for r in range(R):
		#	theta_misp+=misprediction_count(model, data, subject, max_action=A)
		misp[i,0]=theta
		misp[i,1]=np.mean(theta_misps)#theta_misp/R
		misp[i,2]=np.std(theta_misps)
	
		#print misp[i,:]

	return min(misp, key=lambda x: x[1])


def load_data(group):
	if group=='kids':
		data=Data.Data(parameters.inputfile_kids)
	elif group=='adults':
		data=Data.Data(parameters.inputfile_adults)
	else:
		print 'Unknown group.'
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
		model_actions=model.choose_actions(subject, i)#, subject_sequence[:i-1])
		#model_actions=adata[subject][i]['TMA']#model.choose_action(subject_sequence[:i-1])
		if subject_sequence[-1].get_action() not in model_actions:
			mispredictions[i]=1

	return np.mean(mispredictions)




if __name__ == '__main__':
	#cProfile.run('main()')
	#main_global(group='kids', filename='td_kids_A10.pkl', N=31)

	#main_global(group='adults', filename='td_adults_A10.pkl', N=98)
	#main_global(filename='td_adults_10A.pkl'N=98)
	
	#kids
	group='kids'
	filename='td_kids_A10.pkl'
	#main_global(group, filename)
	main_individual(group, filename, N=parameters.n_kids)

	#adults
	group='adults'
	filename='td_adults_A10.pkl'
	#main_global(group, filename)
	#main_individual(group, filename, N=parameters.n_adults)
