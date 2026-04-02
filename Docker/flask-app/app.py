from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask version 1.0 "

@app.route("/hello")
def hello():
    return "Hello Endpoint Welcome!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)