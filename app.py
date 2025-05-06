import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Aira Wence Aranzado, BSIT III-A, System Integration and Architecture - semi-final exam'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)