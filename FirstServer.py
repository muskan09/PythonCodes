from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs


messages = []


response = """
		<html>
			<body>
				<h1> Message Board </h1>
				<form action="/" method="post">
					<textarea name="message"></textarea> </br>
					<button type="submit">Submit</button>
				</form>
				<h2> Message List </h2>
				<ul>
				{}
				</ul>
			</body>
		</html>
		"""

def createList(arr):
	response = ""
	for _ in arr:
		response += "<li>{}</li>".format(_)
	return response

class FirstServer(BaseHTTPRequestHandler):

	def do_POST(self):
		length = int(self.headers.get('Content-Length',0))
		data = self.rfile.read(length).decode()
		message = parse_qs(data)['message'][0]
		messages.append(message)
		self.send_response(200)
		self.send_header('Content-Type', 'text/html; charset=utf-8')
		self.end_headers()
		self.wfile.write(response.format(createList(messages)).encode())


	def do_GET(self):
		self.send_response(200)
		# Starting of the Headers
		self.send_header('Content-Type', 'text/html; charset=utf-8')
		self.end_headers()
		# Now, below we will write the response body

		
		self.wfile.write(response.format(createList(messages)).encode())

	



if __name__ == "__main__":
	try:
		server_address = ('',8002)
		http_d = HTTPServer(server_address,FirstServer)
		http_d.serve_forever()
	except KeyboardInterrupt:
		http_d.socket.close()