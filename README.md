# Intelligent Hacking
Idea inspired from [Stealing PINs via Mobile Sensors](https://arxiv.org/pdf/1605.05549.pdf). This project is created to demonstrate the power of ML with IoT. Uhuru's [Milkcocoa](https://mlkcca.com/) is used to developed this app.
Runs using SimpleRNN on the server or edge side. Collects accelerometer's data on mobile using js through Milkcocoa's js api.

## Running the code:

### Running the server client code: 
> $ `git clone https://github.com/BSatyaKishore/Intelligent-Hacking`
> $ `cd Intelligent-Hacking`
> $ `python -m SimpleHTTPServer`

### Running the ML component: 
To be ran on the device on which computation needs to be done
> $ `cd ML/SDK`
> $ `python Main.py`

### Generating training data:
In `ML/SDK/Main.py:22` (Line 22 of ML/SDK/Main.py), make 
> `Prediction = RNNPredicition.Prediction(self.TrainingData)` 
to
> `Prediction = GenerateTrainingData.Prediction(self.TrainingData)`

The training data will be generated in `ML/SDK/TrainingData`. All the accelerometer data, the clicks and everything will be saved in this file.
#### Training RNN Model:
> $ `cd ML/SDK`
> $ `python RNN-Keras.py`

and the model is saved in `ML/SDK/RNN_model` file.

### Running your models:
> $ `cd ML/SDK`

Create a file with your code in python say `MyModel.py` and create a function like `def Prediction(Data):` in it.

Whenever there is a need of predicition, this function will be called on **a new thread** with the Data.
```
def Prediction(TrainingData):
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
	pa = pred[0].tolist()
	a = pa.index(max(pa))
	return str(a/6)+'_'+str(a%6)
```
is sample RNN model code. Little parsing also needs to be done in the same function.

#### Connecting this with the system:
In `ML/SDK/Main.py:22` (Line 22 of ML/SDK/Main.py), make 
> `Prediction = RNNPredicition.Prediction(self.TrainingData)` 
to
> `Prediction = MyModel.Prediction(self.TrainingData)`

## Demo:
Now, there are two important links:
1. http://localhost:8000/Demo for Demo site.
2. http://localhost:8000/Client for client site. To be opened on mobile phone or device with accelerometer. 
Note: Insert IP and port of the server if accessing remotely.
### Requirements:
> 1. keras on theano backend
> 2. python
> 3. h5py

## Have Fun.


