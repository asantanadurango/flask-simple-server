from distutils.log import debug
from email import message
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def test():
    return jsonify({"message":"success"})

if(__name__ == "__main__"):
    app.run(debug=True, port=4000)