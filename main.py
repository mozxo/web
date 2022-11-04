import requests, os, shutil , time , subprocess, glob
from bs4 import BeautifulSoup

subprocess.Popen(('python3', 'app.py')) 

while True:
  
  result = subprocess.check_output("cd C4C-Yoxmo-LS && git pull", shell=True)
  
  if str(result.decode()).strip('\n') != "Already up to date.":
    files = glob.glob("C4C-Yoxmo-LS/*")
    first = f"""import flask , os
from flask import Flask, render_template , redirect , request

template_dir = os.path.abspath('C4C-Yoxmo-LS')
static_dir = os.path.abspath('C4C-Yoxmo-LS/assets')

app = Flask(__name__, template_folder=template_dir , static_folder=static_dir)

app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
  return render_template('index.html')
""" 
    
    open('route.py', 'w+').write(first)
    
    for item in files:
      if item == "C4C-Yoxmo-LS/index.html":
        pass
      else:
        if item.endswith('html'):
          item = item.strip('C4C-Yoxmo-LS')
          item = item.strip('.html')
          item = item.strip('/')
      
          cleanedr = f"""\n #==== New Route ====#
@app.route('/{item}')
def {item}():
  return render_template('{item}.html')
"""
          open('route.py', 'a+').write(cleanedr)
        pass
    
    print('[*] Added all routes...')
  
  else:
  
    print('[*] No change...')
    time.sleep(1)