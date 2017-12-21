import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time
import urllib2

def SendPrediction(Prediction):
	url = 'https://pubsub1.mlkcca.com/api/push/BJBop-Szz/QvXkGBVhDx8Mzj7G-BTH5Sv9Lo0iPv6ED1zYzKHU?c=ClickDataPrediction&v='+Prediction
	response = urllib2.urlopen(url)
	return

def on_message(ws, message):
	print message
	a = (message.index(":"))
	SendPrediction(message[a+3:-6])

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        return
    thread.start_new_thread(run, ())

if __name__ == "__main__":
	websocket.enableTrace(True)
	ws = websocket.WebSocketApp('wss://pubsub1.mlkcca.com/ws/push/BJBop-Szz/QvXkGBVhDx8Mzj7G-BTH5Sv9Lo0iPv6ED1zYzKHU?c=ClickData',
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
	ws.on_open = on_open
	ws.run_forever()

