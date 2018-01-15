import urllib2
import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time
import threading
import TrueValue, GenerateTrainingData, RNNPredicition

class SendPrediction(threading.Thread):
	def run(self):
		url = 'https://pubsub1.mlkcca.com/api/push/BJBop-Szz/QvXkGBVhDx8Mzj7G-BTH5Sv9Lo0iPv6ED1zYzKHU?c=ClickDataPrediction&v='+self.Prediction
		response = urllib2.urlopen(url)
		return

	def set(self, Prediction):
		self.Prediction = Prediction

class PredictAndSend(threading.Thread):
  def run(self):
    Prediction = GenerateTrainingData.Prediction(self.TrainingData)
    Prediction = RNNPredicition.Prediction(self.TrainingData)
    t3 = SendPrediction()
    t3.set(Prediction)
    t3.start()
    return
  def set(self, TrainingData):
    self.TrainingData = TrainingData

K = False
TrainingData = []
def on_message(ws, message):
  global TrainingData, K
  msg = eval(message)
  # print msg
  if 'clickedId' in message:
    TrainingData = TrainingData + msg
    K = True
  else:
    #print message
    TrainingData = TrainingData + msg
    if K:
      PnS = PredictAndSend()
      PnS.set(TrainingData)
      PnS.start()
      TrainingData = msg
      K = False

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_close1(ws):
    print("### closed Acc Data ###")

def on_open(ws):
    return


class AccData(threading.Thread):
    def run(self):
         #set up and run your first web socket call
         ws = websocket.WebSocketApp('wss://pubsub1.mlkcca.com/ws/send/BJBop-Szz/QvXkGBVhDx8Mzj7G-BTH5Sv9Lo0iPv6ED1zYzKHU?c=AccData',
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close1)
         ws.on_open = on_open
         ws.run_forever()

class ClickData(threading.Thread):
    def run(self):
         #set up and run your second web socket call
         ws = websocket.WebSocketApp('wss://pubsub1.mlkcca.com/ws/push/BJBop-Szz/QvXkGBVhDx8Mzj7G-BTH5Sv9Lo0iPv6ED1zYzKHU?c=ClickData',
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
         ws.on_open = on_open
         ws.run_forever()

if __name__ == "__main__":
    websocket.enableTrace(True)

    t1 = AccData()
    t1.start() 