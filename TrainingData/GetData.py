import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time
import threading

def on_message(ws, message):
    print (message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    return


class T1(threading.Thread):
    def run(self):
         #set up and run your first web socket call
         ws = websocket.WebSocketApp('wss://pubsub1.mlkcca.com/ws/send/BJBop-Szz/QvXkGBVhDx8Mzj7G-BTH5Sv9Lo0iPv6ED1zYzKHU?c=AccData',
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
         ws.on_open = on_open
         ws.run_forever()

class T2(threading.Thread):
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

    t1 = T1()
    t1.start() 

    # t2 = T2()
    # t2.start()
