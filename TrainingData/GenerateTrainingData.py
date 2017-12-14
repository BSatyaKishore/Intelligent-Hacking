import sys, time
import milkcocoa.milkcocoa as milkcocoa

milkcocoaClient = milkcocoa.Milkcocoa.connect("dogjb65ykxo")

datastore0 = milkcocoaClient.datastore("ClickData")
datastore1 = milkcocoaClient.datastore("AccData")

def on_push(e):
	print e

datastore0.on("push",on_push)
datastore1.on("send",on_push)

while(True):
	time.sleep(1)
