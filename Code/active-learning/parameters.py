
import platform

if platform.system()=='Darwin':
	#directory='/Users/alejo/Neuro/ActiveLearning/'
	directory='/Users/alejo/Projects/ActiveLearning/'
elif platform.system()=='Linux':
	#directory='/home/alejo/Run/active-learning/'
    directory='/home/alejo/Neuro/ActiveLearning/'

inputfile_kids=directory+'Data/CPF2_Transcribed112114-CSV.csv'
inputfile_adults=directory+'Data/compiledv2_Headers.csv'

output_directory=directory+'Output/Adults/'

n_kids=98#31#31#5#5#1#29 #31 total, use 40
#truncate=75
#n_r_theo=1#5
n_r_random=2#20#20#20#0#50

epsilon=1e-3
