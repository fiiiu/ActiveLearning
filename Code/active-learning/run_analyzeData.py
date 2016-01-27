import os
import time 
import AnalyzedData


if os.path.isfile('td.pkl'):
	os.remove('td.pkl')

ad=AnalyzedData.AnalyzedData('td_adults_2_10.pkl', 'adults', N=2, A=10)


starttime=time.clock()
ad.analyze()

print 'time elapsed for analysis: {0:.0f} s'.format(time.clock()-starttime)


ad.save()

print ad.alldata

