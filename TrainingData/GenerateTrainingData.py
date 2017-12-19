import sys, time, random
import milkcocoa.milkcocoa as milkcocoa

milkcocoaClient = milkcocoa.Milkcocoa.connect("dogjb65ykxo")

datastore0 = milkcocoaClient.datastore("ClickData")
datastore1 = milkcocoaClient.datastore("AccData")

def on_push(e):
	print>>sys.stderr, e

datastore0.on("push",on_push)
datastore1.on("send",on_push)

while True:
	print str(random.randint(1, 12))+str(random.randint(1, 6))
	time.sleep(2)
