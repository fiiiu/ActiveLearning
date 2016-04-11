import os
import time 
import AnalyzedData
import parameters 

if os.path.isfile('td.pkl'):
	os.remove('td.pkl')

ad=AnalyzedData.AnalyzedData('td_kids_A10.pkl', 'kids', N=parameters.n_kids, A=10)
#ad=AnalyzedData.AnalyzedData('td_adults_A10.pkl', 'adults', N=parameters.n_adults, A=10)


starttime=time.clock()
ad.analyze()

print 'time elapsed for analysis: {0:.0f} s'.format(time.clock()-starttime)


ad.save()

#print ad.alldata

