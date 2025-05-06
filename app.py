from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Aira Wence Aranzado, BSIT III-A, System Integration and Architecture - semi-final exam'
