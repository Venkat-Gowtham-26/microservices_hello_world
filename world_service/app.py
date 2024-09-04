from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/world')
def world():
    return "World"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
