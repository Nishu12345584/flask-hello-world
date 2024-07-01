from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# This allows Lambda to load the Flask app
def lambda_handler(event, context):
    return app(event, context)

