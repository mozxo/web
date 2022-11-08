import flask , os
from flask import Flask, render_template , redirect , request

template_dir = os.path.abspath('web')
static_dir = os.path.abspath('web/assets')

app = Flask(__name__, template_folder=template_dir , static_folder=static_dir)

app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
  return render_template('index.html')

if '__main__' == __name__:
    app.run(host='0.0.0.0', port='5000', debug=True)
  