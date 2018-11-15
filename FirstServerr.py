from http.server import HTTPServer, BaseHTTPRequestHandler
#this class is for:until and unless we dont mention server adress itll work on this particular port..server listens infinetly to port 8001..all request handlers are in this class
class FirstServer(BaseHTTPRequestHandler):
	def do_GET(self):
#starting of the headers we dont need to specify http req now 200 status code for OK
		self.send_response(200)
    	self.send_header('Content-Type', 'text/plain; charset=utf-8')
		self.end_headers()
		self.wfile.write(response.encode())

if __name__ == "__main__":
		server_address=('',8001) #to listen to server,on which adress would the server work,works on local address by default
		http_d = HTTPServer(server_address,FirstServer)
		http_d.serve_forever()
