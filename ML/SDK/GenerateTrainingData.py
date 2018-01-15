import random

def Prediction(TrainingData):
	f = open('TrainingData','a')
	print>>f, TrainingData
	print len(TrainingData)
	f.close()
	a = str(random.randint(0,12))+'_'+str(random.randint(0,6))
	print a
	return a