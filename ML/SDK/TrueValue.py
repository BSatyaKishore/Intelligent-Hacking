def Prediction(TrainingData):
	message = str(TrainingData[-1])
	a = (message.index(":"))
	print 'Sending :',(message[a+2:-4])
	return (message[a+2:-4])
