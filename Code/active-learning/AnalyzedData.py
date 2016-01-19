
import cPickle as pkl
import os
import parameters
import Data
import learners
import entropy_gains

class AnalyzedData():

	def __init__(self, filename, N=None, A=None):

		self.filename=filename
		#check nonexistent filename
		if os.path.isfile(self.filename):
			print "Initialized with existing file. WILL NOT SAVE."
		
		if N is None:
			N=parameters.n_kids
		else:
			self.N=N
		
		if A is None:
			self.A=10
		else:
			self.A=A

		self.alldata={}
		

	def analyze(self):
		data=self.load_data()
		subjects=data.get_kids()[:self.N]

		for subject in subjects:
			print 'Analyzing subject {0}...'.format(subject)
			self.alldata[subject]={}#defaultdict(dict)
			max_action=min(data.get_kid_nactions(subject),self.A)
			subject_sequence=data.data[subject][:max_action]

			for actioni in range(max_action):
				#print 'Action {0} of {1}'.format(actioni, max_action)
				self.alldata[subject][actioni]={}
				subject_action=data.data[subject][actioni].get_action()
				self.alldata[subject][actioni]['SA']=subject_action
				
				theory_model=learners.TheoryLearner()
				model_actions, model_gain=theory_model.choose_actions(subject_sequence[:actioni])
				
				self.alldata[subject][actioni]['TMA']=model_actions

				self.alldata[subject][actioni]['SEIG']=\
					entropy_gains.theory_expected_final_entropy(subject_action, subject_sequence[:actioni])
			
				self.alldata[subject][actioni]['TMEIG']=model_gain
				
				pg_model=learners.ActivePlayer()
				model_actions, model_gain=pg_model.choose_actions(subject_sequence[:actioni])

				self.alldata[subject][actioni]['PMA']=model_actions
				self.alldata[subject][actioni]['PMSP']=model_gain

			self.save()


	def load_data(self):
		data=Data.Data(parameters.inputfile_kids)
		data.read(astext=False)
		return data

	def safe_save(self):
		#check nonexistent filename
		if not os.path.isfile(self.filename):
			with open(self.filename, 'wb') as f:
				pkl.dump(self.alldata, f)
		else:
			print 'FILE EXISTS, NOT SAVING.'

	def save(self):
		with open(self.filename, 'wb') as f:
			pkl.dump(self.alldata, f)
		
	def load(self):
		with open(self.filename, 'rb') as f:
			self.alldata=pkl.load(f)

