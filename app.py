#This code is form https://github.com/LondheShubham153/flask-app-ecs/blob/main/app.py
#Running again due to intial syntax error in lint.yml file and setup python 
#Added error this time to check
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
    return none
    if go


@app.route('/health')
def health():
    return 'Server is up and running'
