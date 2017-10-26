from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['DEBUG'] = True #every time you run an error, it will show an error message; without this line, the server will crash and you won't know why

@app.route('/')
def home():
	return render_template('me.html', name='ALICE', my_friends={'jonathan': 68, 'cesar': 62, 'nick': 100})

@app.route('/login')
def login(): #create decorator
	return render_template('login.html')

if __name__ == "__main__": #main is magic variable
	app.run() 
	