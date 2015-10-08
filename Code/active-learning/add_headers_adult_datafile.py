
fout=open('/Users/alejo/Projects/ActiveLearning/Data/compiledv2_Headers.csv', 'w')

with open('/Users/alejo/Projects/ActiveLearning/Data/compiledv2.txt', 'r') as f:
	for i,line in enumerate(f):
		fout.write("{0},{1}".format(i,line))

fout.close()






