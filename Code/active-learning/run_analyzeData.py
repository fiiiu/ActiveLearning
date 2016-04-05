import os
import time 
import AnalyzedData


if os.path.isfile('td.pkl'):
	os.remove('td.pkl')

<<<<<<< Updated upstream
ad=AnalyzedData.AnalyzedData('td_adults_2_10.pkl', 'adults', N=2, A=10)
=======
ad=AnalyzedData.AnalyzedData('td_adults_A10.pkl', 'adults', N=98, A=10)
>>>>>>> Stashed changes


starttime=time.clock()
ad.analyze()

print 'time elapsed for analysis: {0:.0f} s'.format(time.clock()-starttime)


ad.save()

print ad.alldata

