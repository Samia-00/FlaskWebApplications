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
	
	
if __name__ == '__main__':
      app.run(debug=True)
