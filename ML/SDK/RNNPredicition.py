import numpy as np

from keras.models import Sequential, load_model
from keras.layers import Dense
from keras.layers import LSTM

model = load_model('RNN_model')
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
	TrainingDataX = TrainingData[-6:-1]
	pred = model.predict(np.array([TrainingDataX]))
	# print pred
	pa = pred[0].tolist()
	a = pa.index(max(pa))
	print a, a/6, a%6 
	print str(a/6)+'_'+str(a%6)
	return str(a/6)+'_'+str(a%6)

