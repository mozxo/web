import flask , os
from flask import Flask, render_template , redirect , request

template_dir = os.path.abspath('C4C-Yoxmo-LS')
static_dir = os.path.abspath('C4C-Yoxmo-LS/assets')

app = Flask(__name__, template_folder=template_dir , static_folder=static_dir)

app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
  return render_template('index.html')

 #==== New Route ====#
@app.route('/home')
def home():
  return render_template('home.html')

 #==== New Route ====#
@app.route('/login')
def login():
  return render_template('login.html')

 #==== New Route ====#
@app.route('/register')
def register():
  return render_template('register.html')

 #==== New Route ====#
@app.route('/setting')
def setting():
  return render_template('setting.html')
