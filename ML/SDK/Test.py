import urllib2

def SendPrediction(Prediction):
	url = 'https://pubsub1.mlkcca.com/api/push/BJBop-Szz/QvXkGBVhDx8Mzj7G-BTH5Sv9Lo0iPv6ED1zYzKHU?c=ClickDataPrediction&v='+Prediction
	response = urllib2.urlopen(url)
	return

SendPrediction('1_2')