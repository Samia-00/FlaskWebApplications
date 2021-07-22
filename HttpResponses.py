from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
       return '<h1>Bad Request</h1>', 400

from flask import make_response
@app.route('/samia')
def index1():
	response = make_response('<h1>This document carries a cookie!</h1>')
	response.set_cookie('answer', '42')
	return response


from flask import redirect
@app.route('/github')
def index2():
	return redirect('https://github.com/Samia-00')	
	
	
from flask import abort

@app.route('/user/<id>')
def get_user(id):
	user = load_user(id)
	if not user:
		abort(404)
		return '<h1>Hello, %s</h1>' % user.name
		
		
if __name__ == '__main__':
      app.run(debug=True)
