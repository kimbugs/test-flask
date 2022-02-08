import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps({
        'name': 'kimbugs',
        'email': 'kimbugs@naver.com'
    })
app.run()