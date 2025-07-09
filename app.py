# Flask app entry point
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Ansible Web UI'

if __name__ == '__main__':
    app.run(debug=True)
