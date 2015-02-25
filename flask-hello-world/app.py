# ---- Flask Hello World ---- #

# import the Flask class from the flask module
from flask import Flask

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
@app.route('/hello')

# define the view using a function to a url
def hello_world():
	return "Hello, World!"

# star the development server using the run() method
if __name__ == "__main__":
	app.run()