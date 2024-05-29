from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello Developer✌</h1>"

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
