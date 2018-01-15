# Parsing
if True:
	# Fills this array
	TrainingData = []

	f = open('TrainingData','r')

	def fun(i):
		if len(i) == 1:
			return [i[0].split(':')[-1][1:-1]]
		return [float(j[4:]) for j in i]

	oldI = 0
	lk = 0
	sk = 0
	for line in f.readlines():
		_Temp = []
		lk = lk+1
		data = eval(line[:-1])
		data.sort(key=lambda tup: tup[0])
		for i in data:
			a = fun(i[1][1:-1].split(','))
			_Temp.append(a)
			if 'clickedId' in str(i):
					break
		TrainingData.append(_Temp)
		print 'LK', lk

	f.close()

# Running RNN on the data
import keras
import matplotlib.pyplot as plt
import numpy as np
import time
import csv
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential

def String2Array(string):
	Nums = string.split('_')
	number = int(Nums[0])*6+int(Nums[1])
	Array = [0]*120
	Array[number] = 1
	return Array

def MyMetric(y_true, y_pred):
	val = 0
	#pred = y_pred.tolist()
	pred = y_pred.argmax() #(max(y_pred))
	true = y_true.argmax()
	(x_t, y_t) = (true/6, true%6)
	(x_p, y_p) = (pred/6, pred%6)
	return ((x_t-x_p)**2 + (y_t-y_p)**2)**0.5

def SplitTrainingData(TrainingData):
	TrainingDataX = [i[-8:-1] for i in TrainingData]
	TrainingDataY = [String2Array(i[-1][0]) for i in TrainingData]
	TrainingDataX = np.array(TrainingDataX)
	print TrainingDataX.shape
	return (TrainingDataX, TrainingDataY)

def build_model():
    model = Sequential()
    layers = [3, 20, 150, 120]

    model.add(LSTM(
        layers[1],
        input_shape=(7, 3),
        return_sequences=True))
    model.add(Dropout(0.1))

    model.add(LSTM(
        layers[2],
        return_sequences=False))
    model.add(Dropout(0.5))

    model.add(Dense(
        layers[3]))
    model.add(Activation('sigmoid'))

    adam = keras.optimizers.Adamax(lr=0.01, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
    start = time.time()
    model.compile(loss="categorical_crossentropy", optimizer=adam, metrics=[MyMetric])
    print "Compilation Time : ", time.time() - start
    return model

if True:
	print 'About to start'
	model = build_model()
	TrainingDataX, TrainingDataY = SplitTrainingData(TrainingData)
	model.fit(
	    TrainingDataX, TrainingDataY,
	    batch_size=1, nb_epoch=100, validation_split=0.15)
	model.save('RNN_model')