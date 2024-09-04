from flask import Flask
import requests

app = Flask(__name__)

@app.route('/hello-world')
def hello_world():
    try:
        hello_response = requests.get('http://127.0.0.1:49579/hello')
        hello_response.raise_for_status()
        world_response = requests.get('http://127.0.0.1:49587/world')
        world_response.raise_for_status()

        hello_message = hello_response.text
        world_message = world_response.text

        return f"{hello_message} {world_message}"
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
