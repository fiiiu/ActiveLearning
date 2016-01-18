
import platform

if platform.system()=='Darwin':
	#directory='/Users/alejo/Neuro/ActiveLearning/'
	directory='/Users/alejo/Projects/ActiveLearning/'
elif platform.system()=='Linux':
	#directory='/home/alejo/Run/active-learning/'
    directory='/home/alejo/Neuro/ActiveLearning/'

inputfile_kids=directory+'Data/CPF2_Transcribed112114-CSV.csv'
inputfile_adults=directory+'Data/compiledv2_Headers.csv'

output_directory=directory+'Output/Adults/151103/'

n_kids=31#31#5#5#1#29 #31 kids, 98 adults.
n_adults=98
#truncate=75
#n_r_theo=1#5
n_r_random=20#20#20#20#0#50

epsilon=1e-3
