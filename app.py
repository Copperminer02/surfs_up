# Import Dependencies
from flask import Flask

# Crewate new Flask App Instance
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'