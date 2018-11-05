from flask import Flask, jsonify
app = Flask(__name__)  # Flask running as imported object in program

@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    return "hello, {}".format(name)

if __name__ == "__main__":
    app.run(host="127.0.0.1")
