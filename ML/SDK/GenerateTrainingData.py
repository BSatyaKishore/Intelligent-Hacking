def Prediction(TrainingData):
	f = open('TrainingData','a')
	print>>f, TrainingData
	print len(TrainingData)
	f.close()
	return '10_1'