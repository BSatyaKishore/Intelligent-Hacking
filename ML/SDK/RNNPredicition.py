import numpy as np
import random
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras.layers import LSTM

def MyMetric(y_true, y_pred):
	pred = y_pred.argmax() #(max(y_pred))
	true = y_true.argmax()
	(x_t, y_t) = (true/6, true%6)
	(x_p, y_p) = (pred/6, pred%6)
	return ((x_t-x_p)**2 + (y_t-y_p)**2)**0.5

model = load_model('RNN_model', custom_objects={'MyMetric': MyMetric})
print 'Model loaded'

def fun(i):
	if len(i) == 1:
		return [i[0].split(':')[-1][1:-1]]
	return [float(j[4:]) for j in i]

def Prediction(TrainingData):
	# print TrainingData, len(TrainingData)
	_Temp = []
	TrainingData.sort(key=lambda tup: tup[0])
	for i in TrainingData:
		a = fun(i[1][1:-1].split(','))
		_Temp.append(a)
		oldI = i[0]
		if 'clickedId' in str(i):
			break
	TrainingData = _Temp
	TrainingDataX = TrainingData[-8:-1]
	pred = model.predict(np.array([TrainingDataX]))
	# print pred
	pa = pred[0].tolist()
	a = pa.index(max(pa))
	print 'Predicition :', a, a/6, a%6 
	#print str(a/6)+'_'+str(a%6)
	return str(a/6)+'_'+str(a%6)

