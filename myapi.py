from flask import Flask, request, jsonify


app = Flask(__name__)

id = 0

class Joke():

	def __init__(self, category, data):
		global id
		self.category = category
		self.data = data
		self.id = id
		id += 1

	def serialize(self):
		return {
			'category': self.category,
			'data': self.data,
			'id': self.id
		}

	def edit(self, category, data):
		self.category = category
		self.data = data

jokes_list = []


@app.route('/', methods=['POST'])
def hello_world():
    return jsonify(jokes=[ _.serialize() for _ in jokes_list])

@app.route('/add', methods=['PUT', 'get'])
def add_joke():
	if request.method == 'PUT':
		data = request.form['data']
		category = request.form['category']
		jokes_list.append(Joke(category=category, data=data))
		return jsonify(jokes_list[-1].serialize())
	return "Hello Joke"

@app.route('/update/<int:id>', methods=['PATCH'])
def edit_joke(id):
	for i in range(len(jokes_list)):
		if jokes_list[i].id == id:
			if 'category' in request.form and 'data' in request.form:
				jokes_list[i].edit(request.form['category'], request.form['data'])
				return jsonify(jokes=[_.serialize() for _ in jokes_list])
	return jsonify(error="Error aaya hai!")


if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0", port=5000)