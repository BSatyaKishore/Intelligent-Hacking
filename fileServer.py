import BaseHTTPServer, SimpleHTTPServer
import ssl

class CORSRequestHandler (SimpleHTTPServer.SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)
'''
httpd = BaseHTTPServer.HTTPServer(('localhost', 3610),
        SimpleHTTPServer.SimpleHTTPRequestHandler)
'''

httpd = BaseHTTPServer.HTTPServer(('localhost', 3610), 
	CORSRequestHandler, 
	SimpleHTTPServer.SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket,
        keyfile="./key.pem",
        certfile='./cert.pem', server_side=True)

httpd.serve_forever()
