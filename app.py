from flask import Flask

app = Flask(__name__)

@app.route('/')
def Index():
    return 'Hello World from Python Flask!'
exit()    