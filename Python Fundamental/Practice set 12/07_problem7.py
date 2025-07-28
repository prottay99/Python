from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="color:red">Hello, World! Welcome to Dev world</h1>'

if __name__ == '__main__':
    app.run(debug=True)
