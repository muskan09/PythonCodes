from http.server import HTTPServer, BaseHTTPRequestHandler

class FirstServer(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		# starting of headers
		self.send_header('Content-Type', 'text/html; charset=utf-8')
		self.end_headers()
		# now below we'll write the response body
	  
		response = """
		<html>
			<body>
				<h1> My Server </h1>
			</body>
                        <form action="/" method="post">
                        <textarea name="message"></textarea> </br>
                        <button type="submit"> Submit </button>
                        </form>
		</html>
		"""
		self.wfile.write(response.encode())

	def do_POST(self):
		length = int(self.headers.get('Content-Length',0))
		data = self.rfile.read(length).decode()
		print(data)
		self.send_response(200)
		self.send_header('Content-Type', 'text/html; charset=utf-8')
		self.end_headers()
		self.wfile.write(response.encode())
		

if __name__ == "__main__":
	server_address = ('' ,8001)
	http_d = HTTPServer(server_address, FirstServer)
	http_d.serve_forever()
