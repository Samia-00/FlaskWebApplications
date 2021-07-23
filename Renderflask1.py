from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
    
app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'k4jomei0sxzb680v'

@app.route('/')
@app.route('/index')
def index():

	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	
	return render_template('user.html', name=name)
	
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404	
	
if __name__ == '__main__':
	app.run(debug=True)
