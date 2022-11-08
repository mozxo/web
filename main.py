import requests, os, shutil , time , subprocess, glob
from bs4 import BeautifulSoup

name = input('[?] Enter name: ')

if len(glob.glob(f"web/*")) <= 1:
  os.system(f'git clone https://github.com/{name}/VSCode-Browser-Webserver.git')
else:
  pass

def addroutes():
  files = glob.glob(f"web/*")
  first = f"""import flask , os
from flask import Flask, render_template , redirect , request

template_dir = os.path.abspath('web')
static_dir = os.path.abspath('web/assets')

app = Flask(__name__, template_folder=template_dir , static_folder=static_dir)

app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
  return render_template('index.html')
""" 
  
  open('app.py', 'w+').write(first)
  
  for item in files:
    if item == f"web/index.html":
      pass
    else:
      if item.endswith('html'):
        item = item.strip(f'C4C-{name}-LS')
        item = item.strip('.html')
        item = item.strip('/')
    
        cleanedr = f"""\n #==== New Route ====#
@app.route('/{item}')
def {item}():
  return render_template('{item}.html')
"""
        open('app.py', 'a+').write(cleanedr)
      pass
  
  print('[*] Added all routes...')

  last = f"""\nif '__main__' == __name__:
    app.run(host='0.0.0.0', port='5000', debug=True)
  """ 
    
  open('app.py', 'a+').write(last)



addroutes()

subprocess.Popen(('python3', 'app.py')) 

while True:
  
  result = subprocess.check_output(f"cd web && git pull", shell=True)
  
  if str(result.decode()).strip('\n') != "Already up to date.":
    addroutes()
  else:
    print('[*] No change...')
    time.sleep(1)
